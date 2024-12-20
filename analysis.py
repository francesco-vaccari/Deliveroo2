import os
import importlib.util
import argparse
import re
from collections import defaultdict
from datetime import datetime
import textwrap
from termcolor import colored
import json
import tqdm

def read_files(directory, filenames):
    all_lines = []
    for filename in filenames:
        lines = []
        filepath = os.path.join(directory, filename)
        if os.path.isfile(filepath):
            with open(filepath, 'r') as file:
                lines = file.readlines()
        all_lines.append(lines)
    return all_lines

def extract(line, start_marker, end_marker):
    if end_marker == "":
        start = line.find(start_marker)
        if start == -1:
            return None
        return line[start + len(start_marker):]
    start = line.find(start_marker)
    if start == -1:
        return None
    end = line.find(end_marker, start)
    if end == -1:
        return None
    return line[start + len(start_marker):end]

def print_desires(desires):
    for desire_id, desire in desires.items():
        print(colored(f"Desire {desire_id}: {desire['description']}", 'cyan'))
        for intention in desire['intentions']:
            print(colored(f"    Intention ID: [{intention['id']}]", 'yellow'))
            print(colored(f"        Description: ", 'green') + intention['description'])
            print(colored(f"        Executable at desire end: ", 'green') + str(intention['executable_at_desire_end']))
            print(colored(f"        Executable at experiment end: ", 'green') + str(intention['executable']))
            print(colored(f"        Invalidation reason: ", 'green') + str(intention['invalidation_reason']))
            print(colored(f"        Invalidation after generation reason: ", 'green') + str(intention['invalidation_after_generation_reason']))
            print(colored(f"        Calls: ", 'green') + str(intention['calls']))
            print(colored(f"        Called by: ", 'green') + str(intention['called_by']))
            print(colored(f"        Function:\n", 'green') + textwrap.indent(intention['function'], ' ' * 12))
        print(colored(f"    Executable at experiment end: ", 'magenta') + str(desire['executable']))
        print(colored(f"    Satisfied: ", 'magenta') + str(desire['satisfied']))
        print(colored(f"    Triggered n times: ", 'magenta') + str(desire['triggered_n_times']))
        print(colored(f"    Evaluations: ", 'magenta') + str(desire['evaluations']))
        print(colored(f"    Error: ", 'magenta') + str(desire['error']))
        print(colored(f"    Trigger function:\n", 'magenta') + textwrap.indent(str(desire['trigger_function']), ' ' * 4))
        print()

def print_perception_functions(perception_functions):
    for object_type, functions in perception_functions.items():
        print(colored(f"Object type: {object_type}", 'cyan'))
        for function in functions:
            print(colored(f"    Function:", 'yellow'))
            print(textwrap.indent(function['function'], ' ' * 8))
            print(colored(f"    Error event: ", 'red') + function['error_event'])
        print()

def print_desires_analysis(desires):
    for desire_id in desires:
        print(colored(f"Desire {desire_id}:", 'cyan'))
        for intention in desires[desire_id]['intentions']:
            print(colored(f"    Intention ID: [{intention['id']}]", 'yellow'))
            print(f"        CC: {intention['analysis']['cc']}")
            print(f"        MI: {intention['analysis']['mi']}")
            print(f"        RAW: {intention['analysis']['raw']}")
            print(f"        HAL: {intention['analysis']['hal']}")
        if desires[desire_id]['trigger_function'] is not None:
            print(colored(f"    Trigger function:", 'magenta'))
            print(f"        CC: {desires[desire_id]['trigger_function_analysis']['cc']}")
            print(f"        MI: {desires[desire_id]['trigger_function_analysis']['mi']}")
            print(f"        RAW: {desires[desire_id]['trigger_function_analysis']['raw']}")
            print(f"        HAL: {desires[desire_id]['trigger_function_analysis']['hal']}")
        print()

def print_perception_functions_analysis(perception_functions):
    for object_type in perception_functions:
        print(colored(f"Object type: {object_type}", 'cyan'))
        for function in perception_functions[object_type]:
            print(colored(f"    Function:", 'yellow'))
            print(f"        CC: {function['analysis']['cc']}")
            print(f"        MI: {function['analysis']['mi']}")
            print(f"        RAW: {function['analysis']['raw']}")
            print(f"        HAL: {function['analysis']['hal']}")
        print()

def print_desire_human_analysis(desires_analysis):
    for desire_id, desire in desires_analysis.items():
        print(colored(f"Desire {desire_id}: {desire['n_objectives']} objectives", 'cyan'))
        for intention_id, intention in desire['intentions'].items():
            print(colored(f"    Intention {intention_id}: {intention['n_objectives']} objectives", 'yellow'))
            print(colored(f"    Category: ", 'green') + intention['category'])
            print(colored(f"    One action: ", 'green') + str(intention['one_action']))
        print()

def load_info_from_logs(lines, perception_functions, desires):
    perception_functions_errors = {}
    for line in lines:
        if "Error while processing object type" in line:
            object_type = extract(line, "object type: ", " with event")
            event = extract(line, "event: ", "␤")
            if object_type not in perception_functions_errors:
                perception_functions_errors[object_type] = []
            perception_functions_errors[object_type].append(event)
    
    new_perception_functions = {}
    for object_type, functions in perception_functions.items():
        new_perception_functions[object_type] = []
        for function in functions:
            new_function = {'function': function, 'error_event': None}
            new_perception_functions[object_type].append(new_function)
    for object_type, errors in perception_functions_errors.items():
        for i in range(len(errors)):
            new_perception_functions[object_type][i]['error_event'] = errors[i]
    

    desire_id = None
    desires_satisfaction = {}
    for line in lines:
        if "Desire added: " in line:
            desire_id = extract(line, "Desire added: ", ".")
        if "Desire satisfied␤" in line:
            desires_satisfaction[desire_id] = True
        if "Intention evaluation or intention run failed 3 times" in line:
            desires_satisfaction[desire_id] = False
    
    new_desires = {}
    for desire_id, desire in desires.items():
        new_desires[desire_id] = desire
        new_desires[desire_id]['satisfied'] = desires_satisfaction.get(desire_id, None)
    

    desire_triggered_id = None
    error = False
    desires_triggered = {}
    for line in lines:
        if " is about to be executed ...␤" in line:
            desire_triggered_id = extract(line, "Desire ", " is about to be executed ...␤")
            error = False
            if desire_triggered_id not in desires_triggered:
                desires_triggered[desire_triggered_id] = {'evaluations': [], 'error': False}
        if "Error during intention " in line and " execution. Desire " in line and " is now invalid and intention " in line:
            error = True
        if "Desire triggered evaluated negatively" in line:
            desires_triggered[desire_triggered_id]['error'] = error
            desires_triggered[desire_triggered_id]['evaluations'].append(False)
        if "Desire triggered evaluated positively" in line:
            desires_triggered[desire_triggered_id]['evaluations'].append(True)
    
    for desire_id, desire in new_desires.items():
        if desire_id in desires_triggered:
            desire['triggered_n_times'] = len(desires_triggered[desire_id]['evaluations'])
            desire['error'] = desires_triggered[desire_id]['error']
            desire['evaluations'] = desires_triggered[desire_id]['evaluations']
        else:
            desire['triggered_n_times'] = 0
            desire['error'] = False
            desire['evaluations'] = []
    
            
    current_desire = None
    current_intention = 0
    invalid_intention_at_desire_end = {}
    current_desire_intentions = []
    for line in lines:
        if "Desire added: " in line:
            desire_id = extract(line, "Desire added: ", ".")
            current_desire = desire_id
            invalid_intention_at_desire_end[current_desire] = []
            current_desire_intentions = [intention['id'] for intention in new_desires[current_desire]['intentions']]
        if "Invalidating intention " in line:
            intention_id = extract(line, "Invalidating intention ", " ...␤")
            if current_desire is None:
                # invalidated while executing a triggered desire
                pass
            elif int(intention_id) < int(current_intention) and current_desire is not None:
                # invalidated after being used 3 times in a row in wrong intentions or because uses now invalid intentions
                if intention_id in current_desire_intentions:
                    # but invalidated still during the same desire it was generated in
                    invalid_intention_at_desire_end[current_desire].append(intention_id)
                pass
            else:
                # invalidated after generation, either error or negative evaluation
                invalid_intention_at_desire_end[current_desire].append(intention_id)
                current_intention = intention_id
        if "Generating new desire␤" in line or "Checking if any desire is triggered␤" in line:
            current_desire = None
    
    for desire_id, desire in new_desires.items():
        for i in range(len(desire['intentions'])):
            new_desires[desire_id]['intentions'][i]['executable_at_desire_end'] = True
    
    for desire_id, invalid_intentions in invalid_intention_at_desire_end.items():
        for intention_id in invalid_intentions:
            for intention in new_desires[desire_id]['intentions']:
                if intention['id'] == intention_id:
                    intention['executable_at_desire_end'] = False
    

    current_desire = None
    current_intention = 0
    intentions_invalidation_reasons = {}
    for line in lines:
        if "Desire added: " in line:
            desire_id = extract(line, "Desire added: ", ".")
            current_desire = desire_id
        if "Invalidating intention " in line:
            intention_id = extract(line, "Invalidating intention ", " ...␤")
            if int(intention_id) not in [1, 2, 3, 4, 5, 6]:
                if current_desire is None:
                    # invalidated while executing a triggered desire
                    if intention_id not in intentions_invalidation_reasons:
                        intentions_invalidation_reasons[intention_id] = "desire_triggered_execution"
                    pass
                elif int(intention_id) < int(current_intention) and current_desire is not None:
                    # invalidated after being used 3 times in a row in wrong intentions or because uses now invalid intentions
                    if intention_id not in intentions_invalidation_reasons:
                        intentions_invalidation_reasons[intention_id] = "three_times_in_wrong_intentions_or_dependency"
                    pass
                else:
                    # invalidated after generation, either error or negative evaluation
                    if intention_id not in intentions_invalidation_reasons:
                        intentions_invalidation_reasons[intention_id] = "right_after_generation"
                    current_intention = intention_id
        if "Generating new desire␤" in line or "Checking if any desire is triggered␤" in line:
            current_desire = None
    
    intention_invalidations_after_generation_reasons = {}
    current_intention = None
    for line in lines:
        if "Running intention " in line and " ...␤" in line:
            intention_id = extract(line, "Running intention ", " ...␤")
            current_intention = intention_id
            intention_invalidations_after_generation_reasons[current_intention] = None
        if "Error while running intention generated" in line:
            intention_invalidations_after_generation_reasons[current_intention] = "execution_error"
        if "Obtained evaluation for intention: False␤" in line:
            intention_invalidations_after_generation_reasons[current_intention] = "negative_evaluation"
    
    for desire_id, desire in new_desires.items():
        for intention in desire['intentions']:
            if intention['id'] in intentions_invalidation_reasons:
                intention['invalidation_reason'] = intentions_invalidation_reasons[intention['id']]
            else:
                intention['invalidation_reason'] = None
            if intention['id'] in intention_invalidations_after_generation_reasons:
                intention['invalidation_after_generation_reason'] = intention_invalidations_after_generation_reasons[intention['id']]
            else:
                intention['invalidation_after_generation_reason']

    # if a desire was satisfied but has no trigger function, it means that the generation of the trigger function failed
    # the error for a desire is whether an error happened during the last triggering or if it was because of negative evaluation
    # the length of the evaluations list should be equal to the value of triggered_n_times
    # the invalidation reason for intentions indicates whether if failed right after generation, during a desire trigger, or due to dependecy
    # the invalidation after generation reason is None if the intention was not invalidated after generation, otherwise it shows the cause

    return new_perception_functions, new_desires

def add_intentions_graph(directory, desires):
    calls_dict = defaultdict(list)
    called_by_dict = defaultdict(list)

    with open(os.path.join(directory, 'agent_1', 'result', 'intentions_graph.txt'), 'r') as file:
        for line in file:
            match = re.match(r"- \[(\d+)\] calls : \[(.*)\]", line.strip())
            if match:
                func_id = int(match.group(1))
                calls = [int(x) for x in match.group(2).split(',') if x]
                
                calls_dict[func_id].extend(calls)

                for called_func in calls:
                    called_by_dict[called_func].append(func_id)

    result = {func_id: {'calls': sorted(set(calls)), 'called_by': sorted(set(called_by_dict[func_id]))}
              for func_id, calls in calls_dict.items()}
    
    for func_id in called_by_dict:
        if func_id not in result:
            result[func_id] = {'calls': [], 'called_by': sorted(set(called_by_dict[func_id]))}
    
    for desire_id, desire in desires.items():
        for intention in desire['intentions']:
            intention['calls'] = result[int(intention['id'])]['calls']
            intention['called_by'] = result[int(intention['id'])]['called_by']

    return desires

def fix_data_types(perception_functions, desires):
    new_perception_functions = {}
    for object_type, functions in perception_functions.items():
        new_perception_functions[str(object_type)] = []
        for function in functions:
            function_string = textwrap.dedent(function['function'].strip('\n'))
            error_event = str(function['error_event']).strip(' ').strip('\n')
            new_perception_functions[str(object_type)].append({'function': function_string, 'error_event': error_event})
    
    new_desires = {}
    for desire_id, desire in desires.items():
        new_desires[int(desire_id)] = {}
        new_desires[int(desire_id)]['description'] = desire['description'].strip(' ').strip('\n')
        new_desires[int(desire_id)]['intentions'] = []
        for intention in desire['intentions']:
            new_intention = {}
            new_intention['id'] = int(intention['id'])
            new_intention['description'] = intention['description'].strip(' ').strip('\n')
            new_intention['executable_at_desire_end'] = bool(intention['executable_at_desire_end'])
            new_intention['executable'] = bool("True" in intention['executable']) #
            new_intention['invalidation_reason'] = intention['invalidation_reason']
            new_intention['invalidation_after_generation_reason'] = intention['invalidation_after_generation_reason']
            new_intention['calls'] = [int(call) for call in intention['calls']]
            new_intention['called_by'] = [int(call) for call in intention['called_by']]
            new_intention['function'] = textwrap.dedent(intention['function'].strip('\n'))
            new_desires[int(desire_id)]['intentions'].append(new_intention)
        new_desires[int(desire_id)]['executable'] = bool("True" in desire['executable']) #
        new_desires[int(desire_id)]['satisfied'] = bool(desire['satisfied'])
        new_desires[int(desire_id)]['triggered_n_times'] = int(desire['triggered_n_times'])
        new_desires[int(desire_id)]['evaluations'] = [bool(evaluation) for evaluation in desire['evaluations']]
        new_desires[int(desire_id)]['error'] = bool(desire['error'])
        new_desires[int(desire_id)]['trigger_function'] = textwrap.dedent(desire['trigger_function'].strip('\n').strip(' ').strip('\n'))
        if new_desires[int(desire_id)]['trigger_function'] == "None":
            new_desires[int(desire_id)]['trigger_function'] = None

    return new_perception_functions, new_desires

def load_perception_functions(directory):
    functions_dict = {}
    current_type = None

    with open(os.path.join(directory, 'agent_1', 'result', 'perception_functions.txt'), 'r') as file:
        lines = file.readlines()

    for line in lines:
        # Check if line defines a new type
        type_match = re.match(r"Type:\s+(\w+)", line)
        if type_match:
            current_type = type_match.group(1)
            if current_type not in functions_dict:
                functions_dict[current_type] = []
        # Check if line defines a function
        elif line.strip().startswith("def ") and current_type:
            function_lines = [line]
            # Collect the full function definition
            for next_line in lines[lines.index(line) + 1:]:
                if next_line.strip() == '' or next_line.strip().startswith("Type:"):
                    break
                function_lines.append(next_line)
            # Join the function lines and add to dictionary
            function_code = ''.join(function_lines)
            functions_dict[current_type].append(function_code)
    
    # for func_type, funcs in functions_dict.items():
    #     print(f"{func_type}:")
    #     for func in funcs:
    #         print(func)
            
    return functions_dict

def load_desires(directory):
    desires_dict = {}

    with open(os.path.join(directory, 'agent_1', 'result', 'desires.txt'), 'r') as file:
        lines = file.readlines()
    
    current_desire_id = None
    now_reading_function = False
    now_reading_trigger_function = False
    function_string = ""
    for line in lines:
        if not now_reading_function and not now_reading_trigger_function:
            if "Desire " in line:
                desire_id = extract(line, "Desire ", ":")
                description = extract(line, f"Desire {desire_id}: ", "")
                desires_dict[desire_id] = {}
                desires_dict[desire_id]['description'] = description
                desires_dict[desire_id]['intentions'] = []
                desires_dict[desire_id]['executable'] = False
                desires_dict[desire_id]['trigger_function'] = None
                current_desire_id = desire_id
            if "    Intention ID: [" in line:
                intention_id = extract(line, "    Intention ID: [", "]")
                description = extract(line, f"    Intention ID: {intention_id}: ", "")
                desires_dict[current_desire_id]['intentions'].append({'id': intention_id, 'description': description, 'executable': False})
            if "    Executable: " in line:
                executable = extract(line, "    Executable: ", "")
                desires_dict[current_desire_id]['intentions'][-1]['executable'] = executable
            if "    Description: " in line:
                description = extract(line, "    Description: ", "")
                desires_dict[current_desire_id]['intentions'][-1]['description'] = description
                now_reading_function = True
            if "Executable: " in line:
                executable = extract(line, "Executable: ", "")
                desires_dict[current_desire_id]['executable'] = executable
            if "Trigger function:" in line:
                now_reading_trigger_function = True
        elif now_reading_function:
            function_string += line
            next_line = lines[lines.index(line) + 1]
            if "    Intention ID: " in next_line or "Executable: " in next_line:
                desires_dict[current_desire_id]['intentions'][-1]['function'] = function_string
                function_string = ""
                now_reading_function = False
        elif now_reading_trigger_function:
            function_string += line
            next_line = lines[lines.index(line) + 1]
            if "Desire " in next_line:
                desires_dict[current_desire_id]['trigger_function'] = function_string
                function_string = ""
                now_reading_trigger_function = False
        
    # for desire_id, desire in desires_dict.items():
    #     print(f"Desire {desire_id}: {desire['description']}")
    #     for intention in desire['intentions']:
    #         print(f"    Intention ID: [{intention['id']}]")
    #         print(f"    Description: {intention['description']}")
    #         print(f"    Executable: {intention['executable']}")
    #         print(f"    Function:\n {intention['function']}")
    #     print(f"    Executable: {desire['executable']}")
    #     print(f"    Trigger function:\n {desire['trigger_function']}")

    return desires_dict

def get_cc(function_string):
    with open("temp.py", "w") as f:
        f.write(function_string)
        f.close()
    
    os.system(f"radon cc -s -j temp.py > temp.json")

    with open("temp.json", "r") as f:
        data = json.load(f)
        f.close()
    
    names = []
    ranks = []
    complexities = []
    n_lines = []

    for function in data['temp.py']:
        names.append(function['name'])
        ranks.append(function['rank'])
        complexities.append(function['complexity'])
        n_lines.append(function['endline'] - function['lineno'] + 1)
    
    assert len(names) == len(ranks) == len(complexities) == len(n_lines) == 1
    
    os.system("rm temp.py temp.json")

    # return names[0], ranks[0], complexities[0], n_lines[0]
    return ranks[0], complexities[0]

def get_mi(function_string):
    with open("temp.py", "w") as f:
        f.write(function_string)
        f.close()
    
    os.system(f"radon mi -s -j temp.py > temp.json")

    with open("temp.json", "r") as f:
        data = json.load(f)
        f.close()
    
    mi = data['temp.py']['mi']
    rank = data['temp.py']['rank']

    os.system("rm temp.py temp.json")

    return (mi, rank)

def get_raw(function_string):
    with open("temp.py", "w") as f:
        f.write(function_string)
        f.close()
    
    os.system(f"radon raw -j temp.py > temp.json")

    with open("temp.json", "r") as f:
        data = json.load(f)
        f.close()
    
    lloc = data['temp.py']['lloc']
    sloc = data['temp.py']['sloc']
    comments = data['temp.py']['comments']

    os.system("rm temp.py temp.json")

    return (lloc, sloc, comments)

def get_hal(function_string):
    with open("temp.py", "w") as f:
        f.write(function_string)
        f.close()
    
    os.system(f"radon hal -f -j temp.py > temp.json")
    
    with open("temp.json", "r") as f:
        data = json.load(f)
        f.close()
    
    names = []
    volumes = []
    difficulties = []
    efforts = []
    times = []
    bugs = []
    for function_name, metrics in data['temp.py']['functions'].items():
        names.append(function_name)
        volumes.append(metrics['volume'])
        difficulties.append(metrics['difficulty'])
        efforts.append(metrics['effort'])
        times.append(metrics['time'])
        bugs.append(metrics['bugs'])

    assert len(names) == len(volumes) == len(difficulties) == len(efforts) == len(times) == len(bugs)
    
    os.system("rm temp.py temp.json")

    # return (names, volumes, difficulties, efforts, times, bugs)
    return volumes[0], difficulties[0], efforts[0], times[0], bugs[0]

def parse_date(line):
        match = re.match(r'^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2},\d{3}', line)
        if match:
            return datetime.strptime(match.group(), '%Y-%m-%d %H:%M:%S,%f')
        return None

def perform_human_analysis(desires, directory):
    # print to the user all desires and intention descriptions to get how many objectives the description is made of (int value)
    # print to the user all intention functions to get the category the function belongs to
    # Adaptive, Fixed or Static, Scripted or Predetermined potrebbero essere i nomi delle categorie
    # poi c'è anche la questione delle one-action che è un attributo aggiuntivo per le prime due categorie

    # gli obiettivi possono essere da 1 a n, (ex 1,2,3,4,5,... sono validi input)
    # A, S, P, O sono le categorie che l'utente immette (ex. a, s, p, ao, so, AO, A, S, P, PO sono validi input)

    desire_analysis = load_desire_analysis(directory)
    if desire_analysis is not None:
        print("Desire human analysis already performed. If you want to redo it, please delete the desire_human_analysis.json file.")
        return
    
    desires_analysis = {}
    for desire_id, desire in desires.items():
        desires_analysis[desire_id] = {}
        n = None
        while n is None:
            n = input(colored(f"Desire {desire_id}: {desire['description']}\nHow many objectives does this description contain? ", 'cyan'))
            try:
                n = int(n)
            except ValueError:
                print(colored("Please input a valid integer.", 'red'))
                n = None
        desires_analysis[desire_id]['n_objectives'] = n

        desires_analysis[desire_id]['intentions'] = {}
        for intention in desire['intentions']:
            desires_analysis[desire_id]['intentions'][intention['id']] = {}
            n = None
            while n is None:
                n = input(colored(f"Intention {intention['id']}: {intention['description']}\nHow many objectives does this description contain? ", 'yellow'))
                try:
                    n = int(n)
                except ValueError:
                    print(colored("Please input a valid integer.", 'red'))
                    n = None
            desires_analysis[desire_id]['intentions'][intention['id']]['n_objectives'] = n

            category = None
            one_action = False
            while category is None:
                category = input(colored(f"Intention {intention['id']} function:\n{intention['function']}\nWhich category does the function belong to? (A, S, P, AO, SO, OA, OS) ", 'green'))
                if category.lower() in ['a', 'ao', 'oa', 's', 'so', 'os', 'p']:
                    if 'o' in category.lower():
                        one_action = True
                    if category.lower() in ['a', 'ao', 'oa']:
                        category = 'adaptive'
                    elif category.lower() in ['s', 'so', 'os']:
                        category = 'grounded'
                    elif category.lower() == 'p':
                        category = 'predetermined'
                else:
                    print(colored("Please input a valid category: A, S, P, AO, SO, OA, OS", 'red'))
                    category = None
            desires_analysis[desire_id]['intentions'][intention['id']]['category'] = category
            desires_analysis[desire_id]['intentions'][intention['id']]['one_action'] = one_action
    
    with open(os.path.join(directory, 'agent_1', 'desire_human_analysis.json'), 'w') as f:
        json.dump(desires_analysis, f, indent=4)
    
    print(colored("Human analysis saved to desire_human_analysis.json", 'cyan'))

def load_desire_analysis(directory):
    if not os.path.exists(os.path.join(directory, 'agent_1', 'desire_human_analysis.json')):
        return None
    
    with open(os.path.join(directory, 'agent_1', 'desire_human_analysis.json'), 'r') as f:
        data = json.load(f)
        f.close()
    
    return data

def load_logs(directory):
    filenames = ['agent_1/control.log', 'agent_1/perception.log', 'agent_1/control_manager.log', 'agent_1/perception_manager.log']

    files = read_files(directory, filenames)

    merged_lines = []
    for file in files:
        current_log = ""
        for line in file:
            if parse_date(line):
                if current_log:
                    merged_lines.append(current_log)
                current_log = line
            else:
                current_log += line
        if current_log:
            merged_lines.append(current_log)

    merged_lines.sort(key=lambda x: parse_date(x))

    merged_lines = [line.replace('\n', '␤') for line in merged_lines]

    return merged_lines

def compute_metrics(perception_functions, desires, n=1, total_n=1, typ=1, total_typ=1):
    total_items = sum(len(desire['intentions']) for desire in desires.values()) + len(desires) + sum(len(functions) for functions in perception_functions.values())
    progress_bar = tqdm.tqdm(total=total_items, desc=f"Computing metrics for experiment {n}/{total_n} of typology {typ}/{total_typ}")

    for desire_id, desire in desires.items():
        for intention in desire['intentions']:
            rank, complexity = get_cc(intention['function'])
            mi, rank = get_mi(intention['function'])
            lloc, sloc, comments = get_raw(intention['function'])
            volume, difficulty, effort, time, bugs = get_hal(intention['function'])
            intention['analysis'] = {
                                        'cc': {'rank': rank, 'complexity': complexity},
                                        'mi': {'mi': mi, 'rank': rank},
                                        'raw': {'lloc': lloc, 'sloc': sloc, 'comments': comments},
                                        'hal': {'volume': volume, 'difficulty': difficulty, 'effort': effort, 'time': time, 'bugs': bugs}
                                        }
            progress_bar.update(1)
        if desire['trigger_function'] is not None:
            rank, complexity = get_cc(desire['trigger_function'])
            mi, rank = get_mi(desire['trigger_function'])
            lloc, sloc, comments = get_raw(desire['trigger_function'])
            volume, difficulty, effort, time, bugs = get_hal(desire['trigger_function'])
            desire['trigger_function_analysis'] = {
                                                    'cc': {'rank': rank, 'complexity': complexity},
                                                    'mi': {'mi': mi, 'rank': rank},
                                                    'raw': {'lloc': lloc, 'sloc': sloc, 'comments': comments},
                                                    'hal': {'volume': volume, 'difficulty': difficulty, 'effort': effort, 'time': time, 'bugs': bugs}
                                                    }
        progress_bar.update(1)
    
    for object_type, functions in perception_functions.items():
        for function in functions:
            rank, complexity = get_cc(function['function'])
            mi, rank = get_mi(function['function'])
            lloc, sloc, comments = get_raw(function['function'])
            volume, difficulty, effort, time, bugs = get_hal(function['function'])
            function['analysis'] = {
                                    'cc': {'rank': rank, 'complexity': complexity},
                                    'mi': {'mi': mi, 'rank': rank},
                                    'raw': {'lloc': lloc, 'sloc': sloc, 'comments': comments},
                                    'hal': {'volume': volume, 'difficulty': difficulty, 'effort': effort, 'time': time, 'bugs': bugs}
                                    }
            progress_bar.update(1)
    
    progress_bar.close()

    return perception_functions, desires

if __name__ == "__main__":
    # if the data file exists, load it and skip the analysis
    if os.path.exists("data.json"):
        data = None
        with open('data.json', 'r') as f:
            data = json.load(f)
            f.close()
    else:
        if os.path.exists("temp.json") or os.path.exists("temp.py"):
            print("Please remove temp.json and temp.py from the current directory before running this script.")
            exit()

        experiment_folders = ['1', '2', '3', '4', '5', '6', '7', '8']
        experiment_paths = [os.path.join('experiments', folder) for folder in experiment_folders]

        data = {}

        for i, folder in enumerate(experiment_paths):
            dirs = os.listdir(folder)
            dirs = [d for d in dirs if os.path.isdir(os.path.join(folder, d))]
            total_n = len(dirs)
            n = 1
            data[folder] = []
            for dir in dirs:
                experiment = {'typology': experiment_folders[i], 'path': os.path.join(folder, dir), 'perception_functions': None, 'desires': None, 'desire_analysis': None}
                perception_functions = load_perception_functions(experiment['path'])
                desires = load_desires(experiment['path'])
                logs_lines = load_logs(experiment['path'])
                perception_functions, desires = load_info_from_logs(logs_lines, perception_functions, desires)
                desires = add_intentions_graph(experiment['path'], desires)
                perception_functions, desires = fix_data_types(perception_functions, desires)
                desires_analysis = load_desire_analysis(experiment['path'])
                if desires_analysis is None:
                    print(f"Desire human analysis not performed for experiment {dir}. Exiting.")
                    exit()
                perception_functions, desires = compute_metrics(perception_functions, desires, n=n, total_n=total_n, typ=i+1, total_typ=len(experiment_folders))
                experiment['perception_functions'] = perception_functions
                experiment['desires'] = desires
                experiment['desire_analysis'] = desires_analysis
                data[folder].append(experiment)
                n += 1

        # for folder, experiments in data.items():
        #     print(f"Folder {folder}:")
        #     for experiment in experiments:
        #         print(f"    Experiment {experiment['path']}:")
        #         print(f"        Perception functions: {len(experiment['perception_functions'])}")
        #         print(f"        Desires: {len(experiment['desires'])}")
        #         print(f"        Desire human analysis: {len(experiment['desire_analysis'])}")

        # save the data into a file
        with open('data.json', 'w') as f:
            json.dump(data, f, indent=4)


    for filename in os.listdir('analysis_pipeline'):
        if filename.endswith(".py") and filename != "__init__.py":
            file_path = os.path.join('analysis_pipeline', filename)
            module_name = filename[:-3]
            spec = importlib.util.spec_from_file_location(module_name, file_path)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            if hasattr(module, module_name):
                func = getattr(module, module_name)
                func(data)


# if __name__ == "__main__":    
#     parser = argparse.ArgumentParser(description='Experiment Analysis')
#     parser.add_argument('directory', type=str, help='The experiment directory to analyze')
#     parser.add_argument('--human-analysis', action='store_true', help='Inputs the user with descriptions and functions to perform a human analysis')
#     args = parser.parse_args()

#     perception_functions = load_perception_functions(args.directory)
#     desires = load_desires(args.directory)

#     logs_lines = load_logs(args.directory)
#     perception_functions, desires = load_info_from_logs(logs_lines, perception_functions, desires)
    
#     desires = add_intentions_graph(args.directory, desires)
#     perception_functions, desires = fix_data_types(perception_functions, desires)

#     if args.human_analysis:
#         perform_human_analysis(desires, args.directory)
#         exit()
#     else:
#         desires_analysis = load_desire_analysis(args.directory)
#         if desires_analysis is None:
#             print("Desire human analysis not performed. If you want to perform it, please run the script with the --human-analysis flag.")
#             exit()

#     perception_functions, desires = compute_metrics(perception_functions, desires)
    
#     # print_desires(desires)
#     # print_perception_functions(perception_functions)
#     # print_desires_analysis(desires)
#     # print_perception_functions_analysis(perception_functions)
#     # print_desire_human_analysis(desires_analysis)


# CC score	Rank	Risk
# 1 - 5	    A	    low - simple block
# 6 - 10	B	    low - well structured and stable block
# 11 - 20	C	    moderate - slightly complex block
# 21 - 30	D	    more than moderate - more complex block
# 31 - 40	E	    high - complex block, alarming
# 41+	    F	    very high - error-prone, unstable block

# MI score	Rank	Maintainability
# 100 - 20	A	    Very high
# 19 - 10	B	    Medium
# 9 - 0	    C	    Extremely low

'''
now I need to know about desires:
# - if it was ever satisfied
# - which intentions were valid when the desire was closed
# - if the trigger function was generated correctly
# - if it was ever triggered
# - if it was invalidated after triggering (error or negative evaluation from LLM)

Desire: #satisfied (bool), #intentions_executable_at_end (list of bools), #trigger_function_generated (bool), #triggered (int), #evaluations (list of bools), #evaluations types (last trigger if error or negative evaluation)

about intentions:
# - if it was evaluated as executable (no error and positive evaluation from LLM)
# - if it was invalidated because of error or negative evaluation from LLM
# - if it was invalidated when executing for a triggered desire
# - by which and how many other intentions it calls
# - by which and how many other intentions it was called

about perception functions:
# - the event that triggered the errors

'''
'''
Ovviamente come analisi base vado a vedere in quanti esperimenti l'obiettivo fissato per la categoria è stato effettivamente completato.

Un'altra cosa che posso fare è andare a vedere che tipi di obiettivi vengono proposti dalla LLM, quindi raccogliere parcelle, consegnare, aprire porte, ma anche massimizzare punteggio, navigare efficientemente la mappa, esplorare le celle... e vedere in base all'obiettivo proposto come cambiano le metriche. Forse questo è superfluo perché non mi dice niente di significativo, non mi interessa se con certi elementi specifici all'ambiente la LLM fa meglio o peggio.

Desire:
- satisfied con triggeer function e executable alla fine dell'esperimento (executable at desire end)
- satisfied con trigger function ma non executable alla fine dell'esperimento (numero trigger)
- satisfied senza trigger function
- non satisfied

Intention:
- generazione corretta e executable alla fine dell'esperimento
- generazione corretta ma non executable alla fine dell'esperimento, invalidata durante desire trigger
- generazione corretta ma non executable alla fine dell'esperimento, invalidata per via di dependency
- generazione non corretta per via di errore di esecuzione
- generazione non corretta per via di valutazione negativa

Calcolo metriche per ogni gruppo e posso confrontare average di gruppi diversi. Mi aspetto che codice funzionante abbia metriche migliore o peggiore in certi aspetti rispetto a codice non funzionante.


Mi aspetto che nel corso dell'esperimento le metriche peggiorino per via del fatto che l'agente impara a fare cose più complesse.

Posso comparare codice generato in categorie di esperimento diverse, più elementi nel belief set dovrebbero portare a codice più complesso sia perché ci sono più elementi e anche perché la LLM fa più "fatica" a comprendere l'ambiente.

Mi aspetto che intention che chiamano altre intention implementate prima siano meno complesse e quindi con metriche migliori e mi aspetto anche che abbiano successo più spesso visto che parti sono state confermante come funzionanti in precedenza.




Posso dividere le descrizioni di intention e desire in categorie differenti, in base all'obiettivo che viene descritto. Mi aspetto che intention che hanno obiettivi più complessi abbiano metriche peggiori, sia a livello di desire che a livello di intention.

Posso contare il numero di obiettivi descritti
    
    ex. Desire 1: The agent should strive to collect as many parcels as possible from the parcels spawn point and deliver them to their respective destinations while maintaining a high energy level.
può essere diviso in 3 obiettivi: raccolta, consegna, mantenimento energia
    
    ex. Desire 1: The agent's long term goal is to collect all the keys available on the map, open all the doors and deliver all the parcels to the delivery cell and maximize the score.
può essere diviso in 4 obiettivi: raccolta chiavi, apertura porte, consegna pacchi, massimizzazione punteggio

Maggiore il numero di obiettivi, mi aspetto una complessità maggiore e quindi metriche peggiori. Stessa cosa per intention nel caso specifichino più passaggi. Anche in base al numreo di obiettivi descritti dal desire, posso andare a vedere quanti obiettivi sono contenuti nelle intention generate per quel desire. Mi aspetto che più la tipologia di esperimento è complessa, più obiettivi ci sono nelle intention generate. Un altro modo di contare è semplicemente numero di caratteri nelle descrizioni.
Una cosa da considerare è che intention con molti obiettivi ma che contengono chiamate ad altre intention hanno probabilmente metriche migliore perché appunto sono più corte per via delle intention chiamate.



Infine posso fare una analisi del codice stesso dividendo in categorie il codice generato per le intention. Ad esempio
            def function_7():
                global belief_set
                parcel_coordinates = belief_set['parcel'][1]['coordinates']
                agent_coordinates = belief_set['agent']['coordinates']
                while agent_coordinates != parcel_coordinates:
                    if agent_coordinates[0] < parcel_coordinates[0]:
                        function_2()
                        agent_coordinates[0] += 1
                    elif agent_coordinates[0] > parcel_coordinates[0]:
                        function_1()
                        agent_coordinates[0] -= 1
                    if agent_coordinates[1] < parcel_coordinates[1]:
                        function_4()
                        agent_coordinates[1] += 1
                    elif agent_coordinates[1] > parcel_coordinates[1]:
                        function_3()
                        agent_coordinates[1] -= 1
                function_5()
    non è specifica alle istanze contenute nel belief set, il piano prodotto si adatta alle posizioni dell'agente e delle parcelle

            def function_19():
                global belief_set
                agent_coords = belief_set['agent']['coordinates']
                if belief_set['agent']['energy'] > 50:
                    if agent_coords[0] > 0 and belief_set['map']['grid'][agent_coords[0
                        ] - 1][agent_coords[1]]['cell_type'] == 'walkable':
                        function_1()
                    elif agent_coords[0] < belief_set['map']['width'] - 1 and belief_set[
                        'map']['grid'][agent_coords[0] + 1][agent_coords[1]]['cell_type'
                        ] == 'walkable':
                        function_2()
                    elif agent_coords[1] > 0 and belief_set['map']['grid'][agent_coords[0]
                        ][agent_coords[1] - 1]['cell_type'] == 'walkable':
                        function_3()
                    elif agent_coords[1] < belief_set['map']['height'] - 1 and belief_set[
                        'map']['grid'][agent_coords[0]][agent_coords[1] + 1]['cell_type'
                        ] == 'walkable':
                        function_4()
                else:
                    pass
    questa funzione è generale, ma produce piani con una azione soltanto visto che non ci sono while o for loop, queste intention le chiamo one-action intentions perché producono una solo azione, generalmente sono una lista di if
            
            def function_34():
                global belief_set
                if belief_set['agent']['coordinates'] == [0, 0] and len(belief_set[
                    'agent']['parcels_carried_ids']) > 0:
                    function_6()
                else:
                    function_11()
                if belief_set['agent']['energy'] < 50 and belief_set['agent']['coordinates'
                    ] != [3, 2]:
                    function_2() if belief_set['agent']['coordinates'][0] < [3, 2][0
                        ] else function_1()
                    function_4() if belief_set['agent']['coordinates'][1] < [3, 2][1
                        ] else function_3()
                    function_5()
    questa funzione invece fa riferimento a specifiche coordinate della mappa (ed è anche one-action), quindi è più specifica e meno generica

            def function_25():
                global belief_set
                agent = belief_set['agent']
                if agent['energy'] > 50:
                    function_1()
                    function_2()
                    function_3()
                    function_4()
                    function_5()
                else:
                    pass
    ed infine ci sono funzioni che sono solamente una lista di azioni predeterminate, quindi non soltanto specifiche alla situazione in cui si trova l'agente quando sono generate, ancora più specifiche perché non si basano su coordinate per generare il piano ma il piano viene "generato" direttamente dalla LLM

Una cosa che ho notato è che verso la fine degli esperimenti le funzioni tendono ad essere peggiori (grounded o one-action), questo potrebbe essere dovuto all'accumularsi di oggetti nella mappa che spawnano e quindi che 'mandano in confusione' la LLM che genera azioni meno generiche in quanto meno complesse saltando astrazioni che in altre funzioni fa. Potrebbe essere anche interessante vedere se pure le metriche peggiorano.
'''