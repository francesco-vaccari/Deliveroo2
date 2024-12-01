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
        {'typology': 6, 'path': 'experiments/6/2024-11-15-17-50-00', 'completed': True, 'recognized': True},
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
        print(f'[{i}] Success {success_rate}, recognized {success_recognized_rate}')
        print()



    import matplotlib.pyplot as plt

    typologies_1_to_4 = range(1, 5)
    typologies_5_to_8 = range(5, 9)

    def calculate_rates(typologies):
        success_rates = []
        recognized_rates = []
        for i in typologies:
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
            success_rate = success / total if total > 0 else 0
            recognized_rate = success_recognized / total if total > 0 else 0
            success_rates.append(success_rate)
            recognized_rates.append(recognized_rate)
        return success_rates, recognized_rates

    success_rates_1_to_4, recognized_rates_1_to_4 = calculate_rates(typologies_1_to_4)
    success_rates_5_to_8, recognized_rates_5_to_8 = calculate_rates(typologies_5_to_8)

    plt.figure(figsize=(4, 6))
    plt.plot(typologies_1_to_4, success_rates_1_to_4, label='Success Rate', marker='o')
    plt.xlabel('Typology', fontsize=12)
    plt.ylim(-0.1, 1.1)
    plt.xticks(typologies_1_to_4, fontsize=12)  # Set x-axis values to natural numbers
    plt.yticks(fontsize=12)  # Set y-axis tick fontsize
    plt.legend(fontsize=12)
    plt.tight_layout()
    # plt.show()
    plt.savefig('/Users/francesco/Desktop/Master-Thesis/images/success_rate_1-4.png', dpi=400)
    plt.close()

    plt.figure(figsize=(4, 6))
    plt.plot(typologies_5_to_8, success_rates_5_to_8, label='Success Rate', marker='o')
    plt.xlabel('Typology', fontsize=12)
    plt.ylim(-0.1, 1.1)
    plt.xticks(typologies_5_to_8, fontsize=12)  # Set x-axis values to natural numbers
    plt.yticks(fontsize=12)  # Set y-axis tick fontsize
    plt.legend(fontsize=12)
    plt.tight_layout()
    # plt.show()
    plt.savefig('/Users/francesco/Desktop/Master-Thesis/images/success_rate_5-8.png', dpi=400)
    plt.close()



# Ovviamente come analisi base vado a vedere in quanti esperimenti l'obiettivo fissato per la categoria è stato effettivamente completato.
# Plottare anche mostrando che andando avanti con esperimenti più complessi il success rate diminuisce. 1->2->3->4 e 5->6->7->8