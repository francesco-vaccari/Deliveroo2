import argparse
import os
import json
import matplotlib.pyplot as plt


def get_cc(file_path):
    os.system(f"radon cc -s -j {file_path} > temp.json")
    with open("temp.json", "r") as f:
        data = json.load(f)
        f.close()
    names = []
    ranks = []
    complexities = []
    n_lines = []
    try:
        for function in data[file_path]:
            names.append(function['name'])
            ranks.append(function['rank'])
            complexities.append(function['complexity'])
            n_lines.append(function['endline'] - function['lineno'] + 1)
            print(f"\t\tCC \tRank: {function['rank']}\tComplexity: {function['complexity']}\tLines: {function['endline'] - function['lineno'] + 1}")
    except:
        print(f"\t\t\tNo functions found in {file_path}")
    return (names, ranks, complexities, n_lines)

def get_mi(file_path):
    with open(file_path, "r") as f:
        if f.read() == "":
            print(f"\t\t\tFile {file_path} is empty")
            return (0, 0)
    os.system(f"radon mi -s -j {file_path} > temp.json")
    with open("temp.json", "r") as f:
        data = json.load(f)
        f.close()
    mi = data[file_path]['mi']
    rank = data[file_path]['rank']
    print(f"\t\tMI \tMI: {mi}\tRank: {rank}")
    return (mi, rank)

def get_raw(file_path):
    os.system(f"radon raw -j {file_path} > temp.json")
    with open("temp.json", "r") as f:
        data = json.load(f)
        f.close()
    lloc = data[file_path]['lloc']
    sloc = data[file_path]['sloc']
    comments = data[file_path]['comments']
    print(f"\t\tRaw\tLLOC: {lloc}\tSLOC: {sloc}\tComments: {comments}")
    return (lloc, sloc, comments)

def get_hal(file_path):
    os.system(f"radon hal -f -j {file_path} > temp.json")
    with open("temp.json", "r") as f:
        data = json.load(f)
        f.close()
    
    names = []
    volumes = []
    difficulties = []
    efforts = []
    times = []
    bugs = []
    for function_name, metrics in data[file_path]['functions'].items():
        names.append(function_name)
        volumes.append(metrics['volume'])
        difficulties.append(metrics['difficulty'])
        efforts.append(metrics['effort'])
        times.append(metrics['time'])
        bugs.append(metrics['bugs'])
        print(f"\t\tHal\tVolume: {metrics['volume']}\tDifficulty: {metrics['difficulty']}\tEffort: {metrics['effort']}\tTime: {metrics['time']}\tBugs: {metrics['bugs']}")
    return (names, volumes, difficulties, efforts, times, bugs)

def analyze(folder):
    if os.path.exists("temp.json"):
        print("Warning: temp.json already exists.")
        exit()
    os.system("touch temp.json")

    folder = os.path.join('/experiments', folder)

    agents_folders = []
    agents_names = []

    for element in os.listdir(folder):
        if os.path.isdir(os.path.join(folder, element)):
            if element[0:6] == 'agent_':
                agents_folders.append(os.path.join(folder, element, 'result'))
                agents_names.append(element)

    # folders_to_analyze = ['analyzable_DTF_S', 'analyzable_IF_NW_S', 'analyzable_IF_W_S', 'analyzable_IF_S', 'analyzable_PF_S']
    folders_to_analyze = ['analyzable_DTF_S', 'analyzable_IF_NW_S', 'analyzable_IF_W_S', 'analyzable_PF_S']

    files = {}

    for i in range(len(agents_folders)):
        files[agents_names[i]] = {}
        for folder in folders_to_analyze:
            files[agents_names[i]][folder] = []
            for file in os.listdir(os.path.join(agents_folders[i], folder)):
                if file.endswith('.py'):
                    files[agents_names[i]][folder].append(os.path.join(agents_folders[i], folder, file))

    print("-----------------------------------------------------")
    for agent, agent_files in files.items():
        print(f"Agent: {agent}")
        for file, path in agent_files.items():
            if file.split('.')[0] == 'analyzable_DTF_S':
                name = 'Desire Trigger Functions'
            elif file.split('.')[0] == 'analyzable_IF_NW_S':
                name = 'Intention Functions (Not Working)'
            elif file.split('.')[0] == 'analyzable_IF_W_S':
                name = 'Intention Functions (Working)'
            elif file.split('.')[0] == 'analyzable_PF_S':
                name = 'Perception Functions'
            else:
                name = file.split('.')[0]
            print(f"\n* {name:15}\t\t{[file_path.split('/')[-1].split('.')[0] for file_path in path]}")
            if len(path) == 0:
                # print(f"\tNo files found in {file}")
                pass
            for file_path in path:
                print(f'\t{file_path.split('/')[-1].split('.')[0]}')
                res = get_cc(file_path)
                res = get_mi(file_path)
                res = get_raw(file_path)
                res = get_hal(file_path)
        print("-----------------------------------------------------")

    os.system("rm temp.json")

    # MI: file singoli nelle cartelle
    # CC: file singoli nelle cartelle
    # RAW: file singoli nelle cartelle
    # HAL: file singoli nelle cartelle


def plot_evolution(folder):
    folder = os.path.join('/experiments', folder)

    agents_folders = []
    agents_names = []

    for element in os.listdir(folder):
        if os.path.isdir(os.path.join(folder, element)):
            if element[0:6] == 'agent_':
                agents_folders.append(os.path.join(folder, element, 'result'))
                agents_names.append(element)
    
    print(agents_folders)
    print(agents_names)

    number_desires = []
    number_intentions = []
    number_api_calls = []
    number_desires_working = []
    number_desires_not_working = []
    number_intentions_working = []
    number_intentions_not_working = []
    number_perception_functions = []

    for i in range(len(agents_folders)):
        with open(os.path.join(agents_folders[i], 'evolution_steps.txt'), 'r') as f:
            number_desires = eval(f.readline())
            number_intentions = eval(f.readline())
            number_api_calls = eval(f.readline())
            number_desires_working = eval(f.readline())
            number_desires_not_working = eval(f.readline())
            number_intentions_working = eval(f.readline())
            number_intentions_not_working = eval(f.readline())
            number_perception_functions = eval(f.readline())
            f.close()
        
        assert len(number_desires) == len(number_intentions) == len(number_api_calls) == len(number_desires_working) == len(number_desires_not_working) == len(number_intentions_working) == len(number_intentions_not_working) == len(number_perception_functions)
        n = len(number_intentions)
        steps = [i for i in range(n)]

        plt.plot(steps, number_desires, label='Desires')
        plt.legend()
        plt.title(f"Evolution {agents_names[i]}")
        plt.xlabel("Time (s)")
        plt.ylabel("Number")
        plt.show()
        plt.plot(steps, number_intentions, label='Intentions')
        plt.legend()
        plt.title(f"Evolution {agents_names[i]}")
        plt.xlabel("Time (s)")
        plt.ylabel("Number")
        plt.show()
        plt.plot(steps, number_api_calls, label='API Calls')
        plt.legend()
        plt.title(f"Evolution {agents_names[i]}")
        plt.xlabel("Time (s)")
        plt.ylabel("Number")
        plt.show()
        plt.plot(steps, number_desires_working, label='Desires Working')
        plt.legend()
        plt.title(f"Evolution {agents_names[i]}")
        plt.xlabel("Time (s)")
        plt.ylabel("Number")
        plt.show()
        plt.plot(steps, number_desires_not_working, label='Desires Not Working')
        plt.legend()
        plt.title(f"Evolution {agents_names[i]}")
        plt.xlabel("Time (s)")
        plt.ylabel("Number")
        plt.show()
        plt.plot(steps, number_intentions_working, label='Intentions Working')
        plt.legend()
        plt.title(f"Evolution {agents_names[i]}")
        plt.xlabel("Time (s)")
        plt.ylabel("Number")
        plt.show()
        plt.plot(steps, number_intentions_not_working, label='Intentions Not Working')
        plt.legend()
        plt.title(f"Evolution {agents_names[i]}")
        plt.xlabel("Time (s)")
        plt.ylabel("Number")
        plt.show()
        plt.plot(steps, number_perception_functions, label='Perception Functions')
        plt.legend()
        plt.title(f"Evolution {agents_names[i]}")
        plt.xlabel("Time (s)")
        plt.ylabel("Number")
        plt.show()
        
        
    # Plot results in agent_n/result/evolution_steps.txt
    # Lists in the file are:
    # - numero desires
    # - numero intentions
    # - numero chiamate api
    # - numero desires funzionanti
    # - numero desires non funzionanti
    # - numero intentions funzionanti
    # - numero intentions non funzionanti
    # - numero perception functions



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Deliveroo2 Functions Analysis Tool")
    parser.add_argument('--folder', type=str, required=True, help="Path to the experiment folder")
    parser.add_argument('--analyze', action='store_true', help="Analyze desires, intentions and perception functions")
    parser.add_argument('--plot-evolution', action='store_true', help="Plot evolution steps of the agent")
    args = parser.parse_args()

    if not args.analyze and not args.plot_evolution:
        analyze(args.folder)
        plot_evolution(args.folder)
    elif args.analyze:
        analyze(args.folder)
    elif args.plot_evolution:
        plot_evolution(args.folder)