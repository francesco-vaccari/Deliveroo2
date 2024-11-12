import argparse
import os
import matplotlib.pyplot as plt

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
    args = parser.parse_args()

    plot_evolution(args.folder)