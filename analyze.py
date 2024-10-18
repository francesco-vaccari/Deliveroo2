import argparse
import os
import subprocess
import json

parser = argparse.ArgumentParser(description="Deliveroo2 Functions Analysis Tool")
parser.add_argument('--folder', type=str, required=True, help="Path to the experiment folder")
args = parser.parse_args()

if os.path.exists("temp.json"):
    print("Warning: temp.json already exists.")
    exit()
os.system("touch temp.json")

folder = os.path.join('./experiments', args.folder)

agents_folders = []
agents_names = []

for element in os.listdir(folder):
    if os.path.isdir(os.path.join(folder, element)):
        if element[0:6] == 'agent_':
            agents_folders.append(os.path.join(folder, element, 'result'))
            agents_names.append(element)

# files_to_analyze = ['analyzable_DTF.py', 'analyzable_IF_NW.py', 'analyzable_IF_W.py', 'analyzable_IF.py', 'analyzable_PF.py']
files_to_analyze = []
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
    for file in files_to_analyze:
        files[agents_names[i]][file] = [os.path.join(agents_folders[i], file)]


def get_cc(file_path):
    print(f"\t\tCC")
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
            print(f"\t\t\t{function['name']:15}\t{function['rank']:5}\t{function['complexity']:5}\t{function['endline'] - function['lineno'] + 1:5}")
    except:
        print(f"\t\t\tNo functions found in {file_path}")
    return (names, ranks, complexities, n_lines)

def get_mi(file_path):
    print(f"\t\tMI")
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
    print(f"\t\t\t{mi:5}\t{rank:5}")
    return (mi, rank)

def get_raw(file_path):
    print(f"\t\tRaw")
    os.system(f"radon raw -j {file_path} > temp.json")
    with open("temp.json", "r") as f:
        data = json.load(f)
        f.close()
    
    lloc = data[file_path]['lloc']
    sloc = data[file_path]['sloc']
    comments = data[file_path]['comments']
    print(f"\t\t\t{lloc:5}\t{sloc:5}\t{comments:5}")
    return (lloc, sloc, comments)

def get_hal(file_path):
    print(f"\t\tHal")
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
        print(f"\t\t\t{function_name:15}\t{metrics['volume']:5}\t{metrics['difficulty']:5}\t{metrics['effort']:5}\t{metrics['time']:5}\t{metrics['bugs']:5}")
    return (names, volumes, difficulties, efforts, times, bugs)



print("-----------------------------------------------------")
for agent, agent_files in files.items():
    print(f"Agent: {agent}")
    for file, path in agent_files.items():
        print(f"\n\n* {file.split('.')[0]:15}\t\t{[file_path.split('/')[-1] for file_path in path]}")
        if len(path) == 0:
            # print(f"\tNo files found in {file}")
            pass
        for file_path in path:
            print(f'\t{file_path.split('/')[-1]}')
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