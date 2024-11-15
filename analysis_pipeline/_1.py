def _1(data):
    return
    experiment_completed = [
        {'typology': 1, 'path': 'experiments/1/2024-10-23-17-49-21', 'completed': True, 'recognized': True},
        {'typology': 1, 'path': 'experiments/1/2024-10-23-17-59-47', 'completed': True, 'recognized': True},
        {'typology': 1, 'path': 'experiments/1/2024-10-23-17-41-27', 'completed': True, 'recognized': True},
        {'typology': 2, 'path': 'experiments/2/2024-10-23-18-06-24', 'completed': True, 'recognized': False},
        {'typology': 2, 'path': 'experiments/2/2024-10-23-18-20-19', 'completed': True, 'recognized': True},
        {'typology': 2, 'path': 'experiments/2/2024-10-23-18-16-03', 'completed': True, 'recognized': True},
        {'typology': 3, 'path': 'experiments/3/2024-10-23-20-21-21', 'completed': True, 'recognized': False},
        {'typology': 3, 'path': 'experiments/3/2024-10-23-20-15-43', 'completed': True, 'recognized': False},
        {'typology': 3, 'path': 'experiments/3/2024-10-23-20-30-03', 'completed': True, 'recognized': False},
        {'typology': 4, 'path': 'experiments/4/2024-10-28-09-50-14', 'completed': False, 'recognized': False},
        {'typology': 4, 'path': 'experiments/4/2024-10-28-09-41-36', 'completed': False, 'recognized': False},
        {'typology': 4, 'path': 'experiments/4/2024-10-28-09-31-55', 'completed': True, 'recognized': True},
        {'typology': 5, 'path': 'experiments/5/2024-10-29-15-55-01', 'completed': True, 'recognized': True},
        {'typology': 5, 'path': 'experiments/5/2024-11-01-09-48-01', 'completed': True, 'recognized': True},  
        {'typology': 5, 'path': 'experiments/5/2024-11-02-09-03-00', 'completed': True, 'recognized': True},
        {'typology': 6, 'path': 'experiments/6/2024-11-02-12-00-24', 'completed': True, 'recognized': True},
        {'typology': 6, 'path': 'experiments/6/2024-11-02-10-59-50', 'completed': True, 'recognized': True},
        {'typology': 6, 'path': 'experiments/6/2024-11-02-12-16-06', 'completed': True, 'recognized': True},
        {'typology': 7, 'path': 'experiments/7/2024-11-04-09-33-19', 'completed': True, 'recognized': True},
        {'typology': 7, 'path': 'experiments/7/2024-11-04-11-25-26', 'completed': True, 'recognized': False},
        {'typology': 7, 'path': 'experiments/7/2024-11-14-10-26-25', 'completed': True, 'recognized': False},
        {'typology': 8, 'path': 'experiments/8/2024-11-08-10-51-41', 'completed': False, 'recognized': False},
        {'typology': 8, 'path': 'experiments/8/2024-11-08-17-40-54', 'completed': True, 'recognized': True},
        {'typology': 8, 'path': 'experiments/8/2024-11-07-18-30-26', 'completed': True, 'recognized': False},
    ]

    success = 0
    success_recognized = 0
    total = 0
    for experiment in experiment_completed:
        if experiment['completed']:
            success += 1
            if experiment['recognized']:
                success_recognized += 1
        total += 1

    success_rate = success / total
    success_recognized_rate = success_recognized / success
    recognized_rate = success_recognized / total
    print(f"Total Success rate: {success_rate}")
    print(f"Total Success recognized rate: {success_recognized_rate}")
    print(f"Total Recognized rate: {recognized_rate}")
    print()


    for i in range(1, 9):
        success = 0
        success_recognized = 0
        total = 0
        for experiment in experiment_completed:
            if experiment['typology'] == i:
                if experiment['completed']:
                    success += 1
                    if experiment['recognized']:
                        success_recognized += 1
                total += 1

        success_rate = success / total
        success_recognized_rate = success_recognized / success
        recognized_rate = success_recognized / total
        print(f"[{i}]Success rate: {success_rate}")
        print(f"[{i}]Success recognized rate: {success_recognized_rate}")
        print(f"[{i}]Recognized rate: {recognized_rate}")
        print()




    import matplotlib.pyplot as plt

    # plot success rate and recognized rate for typologyes from 1 to 4
    success_rate = []
    recognized_rate = []
    for i in range(1, 5):
        success = 0
        recognized = 0
        total = 0
        for experiment in experiment_completed:
            if experiment['typology'] == i:
                total += 1
                if experiment['completed']:
                    success += 1
                    if experiment['recognized']:
                        recognized += 1
        success_rate.append(success / total)
        recognized_rate.append(recognized / total)
    
    fig, ax = plt.subplots()
    ax.plot(range(1, 5), success_rate, label='Success rate')
    ax.plot(range(1, 5), recognized_rate, label='Recognized rate')
    ax.set_xlabel('Typology')
    ax.set_ylabel('Rate')
    ax.legend()

    for i in range(1, 5):
        ax.vlines(i, 0, success_rate[i-1], colors='#1f77b4', linestyles='dashed')
    
    for i in range(1, 5):
        ax.vlines(i, 0, recognized_rate[i-1], colors='#ff7f0e', linestyles='dashed')

    plt.show()



    # plot success rate and recognized rate for typologyes from 5 to 7
    success_rate = []
    recognized_rate = []
    for i in range(5, 9):
        success = 0
        recognized = 0
        total = 0
        for experiment in experiment_completed:
            if experiment['typology'] == i:
                total += 1
                if experiment['completed']:
                    success += 1
                    if experiment['recognized']:
                        recognized += 1
        success_rate.append(success / total)
        recognized_rate.append(recognized / total)

    fig, ax = plt.subplots()
    ax.plot(range(5, 9), success_rate, label='Success rate')
    ax.plot(range(5, 9), recognized_rate, label='Recognized rate')
    ax.set_xlabel('Typology')
    ax.set_ylabel('Rate')
    ax.legend()

    for i in range(5, 9):
        ax.vlines(i, 0, success_rate[i-5], colors='#1f77b4', linestyles='dashed')

    for i in range(5, 9):
        ax.vlines(i, 0, recognized_rate[i-5], colors='#ff7f0e', linestyles='dashed')

    plt.show()

    


# Ovviamente come analisi base vado a vedere in quanti esperimenti l'obiettivo fissato per la categoria è stato effettivamente completato.
# Plottare anche mostrando che andando avanti con esperimenti più complessi il success rate diminuisce. 1->2->3->4 e 5->6->7->8