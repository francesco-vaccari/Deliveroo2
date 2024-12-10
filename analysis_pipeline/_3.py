import pandas as pd

def _3(data):
    return
    total_intentions = 0
    total_intentions_executable_at_experiment_end = 0
    total_intentions_generated_correctly = 0
    total_intentions_not_generated_correctly = 0
    total_intentions_generation_execution_error = 0
    total_intentions_generation_negative_evaluation = 0

    generation_failure_by_typology = {}

    n_intentions_by_typology = {}
    generated_correctly_by_typology = {}
    not_generated_correctly_by_typology = {}

    for typology, experiments in data.items():
        generation_failure_by_typology[typology] = {'execution_error': 0, 'negative_evaluation': 0}
        generated_correctly_by_typology[typology] = 0
        not_generated_correctly_by_typology[typology] = 0
        for experiment in experiments:
            experiment_intentions = 0
            experiment_intentions_executable_at_experiment_end = 0
            experiment_intentions_generated_correctly = 0
            experiment_intentions_not_generated_correctly = 0
            experiment_intentions_generation_execution_error = 0
            experiment_intentions_generation_negative_evaluation = 0
            for desire_id, desire in experiment['desires'].items():
                for intention in desire['intentions']:
                    experiment_intentions += 1
                    if intention['executable']:
                        experiment_intentions_executable_at_experiment_end += 1

                    if intention['invalidation_reason'] == 'right_after_generation':
                        experiment_intentions_not_generated_correctly += 1
                        not_generated_correctly_by_typology[typology] += 1
                        if intention['invalidation_after_generation_reason'] == 'negative_evaluation':
                            experiment_intentions_generation_negative_evaluation += 1
                        if intention['invalidation_after_generation_reason'] == 'execution_error':
                            experiment_intentions_generation_execution_error += 1
                    else:
                        experiment_intentions_generated_correctly += 1
                        generated_correctly_by_typology[typology] += 1
            
            # print(f'Experiment intentions: {experiment_intentions}')
            # print(f'Experiment intentions executable at experiment end: {experiment_intentions_executable_at_experiment_end}')
            # print(f'Experiment intentions generated correctly: {experiment_intentions_generated_correctly}')
            # print(f'Experiment intentions not generated correctly: {experiment_intentions_not_generated_correctly}')
            # print(f'Experiment intentions generation execution error: {experiment_intentions_generation_execution_error}')
            # print(f'Experiment intentions generation negative evaluation: {experiment_intentions_generation_negative_evaluation}')

            total_intentions += experiment_intentions
            total_intentions_executable_at_experiment_end += experiment_intentions_executable_at_experiment_end
            total_intentions_generated_correctly += experiment_intentions_generated_correctly
            total_intentions_not_generated_correctly += experiment_intentions_not_generated_correctly
            total_intentions_generation_execution_error += experiment_intentions_generation_execution_error
            total_intentions_generation_negative_evaluation += experiment_intentions_generation_negative_evaluation

            generation_failure_by_typology[typology]['execution_error'] += experiment_intentions_generation_execution_error
            generation_failure_by_typology[typology]['negative_evaluation'] += experiment_intentions_generation_negative_evaluation

            if typology not in n_intentions_by_typology:
                n_intentions_by_typology[typology] = 0
            n_intentions_by_typology[typology] += experiment_intentions

    print(f'Total intentions: {total_intentions}')
    print(f'Total intentions executable at experiment end: {total_intentions_executable_at_experiment_end}')
    print(f'Total intentions generated correctly: {total_intentions_generated_correctly}')
    print(f'Total intentions not generated correctly: {total_intentions_not_generated_correctly}')
    print(f'Total intentions generation execution error: {total_intentions_generation_execution_error}')
    print(f'Total intentions generation negative evaluation: {total_intentions_generation_negative_evaluation}')

    print("All intentions not generated correctly due to execution error had the timeout error.")

    import matplotlib.pyplot as plt

    typologies = list([elem.split('/')[-1] for elem in n_intentions_by_typology.keys()])
    intentions_counts = list(n_intentions_by_typology.values())

    plt.rc('font', size=15)
    plt.rc('axes', axisbelow=True)
    plt.figure(figsize=(9, 6))
    bar_width = 0.7
    plt.bar(typologies, intentions_counts, bar_width, edgecolor='black', color='tab:blue')
    plt.grid(axis='y', linestyle='dashed')
    plt.ylim(-0.1, 81.0)
    plt.yticks(range(0, 81, 5))
    plt.xlabel('Typology')
    plt.ylabel('Number of Intentions')
    plt.tight_layout()
    # plt.show()
    plt.savefig('/Users/francesco/Desktop/Master-Thesis/images/n_intentions.png', dpi=400)
    


    typologies = [typology.split('/')[-1] for typology in generated_correctly_by_typology.keys()]
    generated_correctly = [generated_correctly_by_typology[typology] for typology in generated_correctly_by_typology.keys()]
    not_generated_correctly = [not_generated_correctly_by_typology[typology] for typology in not_generated_correctly_by_typology.keys()]
    plt.close()
    # Plot the data with bars on top of each other
    plt.rc('font', size=15)
    plt.rc('axes', axisbelow=True)
    plt.figure(figsize=(9, 6))
    bar_width = 0.7
    index = range(len(typologies))

    plt.bar(index, generated_correctly, label='Generated Correctly', color='tab:green', width=bar_width, edgecolor='black')
    plt.bar(index, not_generated_correctly, bottom=generated_correctly, label='Not Generated Correctly', color='tab:red', width=bar_width, edgecolor='black')

    plt.xlabel('Typology')
    plt.ylabel('Number of Intentions')
    plt.xticks(index, typologies)
    plt.ylim(-0.1, 81.0)
    plt.yticks(range(0, 81, 5))
    plt.grid(axis='y', linestyle='dashed')
    plt.legend()
    plt.tight_layout()
    # plt.show()
    plt.savefig('/Users/francesco/Desktop/Master-Thesis/images/intentions_generated_vs_not_generated.png', dpi=400)



    typology_averages = {}
    for typology, experiments in data.items():
        num_experiments = len(experiments)
        if num_experiments == 0:
            continue

        typology_averages[typology] = {
            'average_intentions': 0,
            'average_intentions_executable_at_experiment_end': 0,
            'average_intentions_generated_correctly': 0,
            'average_intentions_not_generated_correctly': 0,
            'average_intentions_generation_execution_error': 0,
            'average_intentions_generation_negative_evaluation': 0
        }

        for experiment in experiments:
            experiment_intentions = len([intention for desire in experiment['desires'].values() for intention in desire['intentions']])
            if experiment_intentions == 0:
                continue

            typology_averages[typology]['average_intentions'] += experiment_intentions / num_experiments
            typology_averages[typology]['average_intentions_executable_at_experiment_end'] += sum(1 for desire in experiment['desires'].values() for intention in desire['intentions'] if intention['executable']) / experiment_intentions / num_experiments
            typology_averages[typology]['average_intentions_generated_correctly'] += sum(1 for desire in experiment['desires'].values() for intention in desire['intentions'] if intention['invalidation_reason'] != 'right_after_generation') / experiment_intentions / num_experiments
            typology_averages[typology]['average_intentions_not_generated_correctly'] += sum(1 for desire in experiment['desires'].values() for intention in desire['intentions'] if intention['invalidation_reason'] == 'right_after_generation') / experiment_intentions / num_experiments
            typology_averages[typology]['average_intentions_generation_execution_error'] += sum(1 for desire in experiment['desires'].values() for intention in desire['intentions'] if intention['invalidation_after_generation_reason'] == 'execution_error') / experiment_intentions / num_experiments
            typology_averages[typology]['average_intentions_generation_negative_evaluation'] += sum(1 for desire in experiment['desires'].values() for intention in desire['intentions'] if intention['invalidation_after_generation_reason'] == 'negative_evaluation') / experiment_intentions / num_experiments

    # print('Typology Averages:')
    # for typology, averages in typology_averages.items():
    #     print(f'Typology: {typology}')
    #     for key, value in averages.items():
    #         print(f'{key}: {value:.2f}')
    # print()

    # overall_averages = {
    #     'average_intentions': total_intentions / sum(len(experiments) for experiments in data.values()),
    #     'average_intentions_executable_at_experiment_end': total_intentions_executable_at_experiment_end / total_intentions,
    #     'average_intentions_generated_correctly': total_intentions_generated_correctly / total_intentions,
    #     'average_intentions_not_generated_correctly': total_intentions_not_generated_correctly / total_intentions,
    #     'average_intentions_generation_execution_error': total_intentions_generation_execution_error / total_intentions,
    #     'average_intentions_generation_negative_evaluation': total_intentions_generation_negative_evaluation / total_intentions
    # }

    # print('Overall Averages:')
    # for key, value in overall_averages.items():
    #     print(f'{key}: {value:.2f}')
    # print()


    # import matplotlib.pyplot as plt

    typologies_1_to_4 = [elem.split('/')[-1] for elem in typology_averages.keys() if int(elem.split('/')[-1]) in range(1, 5)]
    typologies_5_to_8 = [elem.split('/')[-1] for elem in typology_averages.keys() if int(elem.split('/')[-1]) in range(5, 9)]

    average_intentions_1_to_4 = [averages['average_intentions'] for typology, averages in typology_averages.items() if int(typology.split('/')[-1]) in range(1, 5)]
    average_intentions_5_to_8 = [averages['average_intentions'] for typology, averages in typology_averages.items() if int(typology.split('/')[-1]) in range(5, 9)]


    # plt.figure(figsize=(10, 6))
    # plt.bar(typologies_1_to_4, average_intentions_1_to_4, label='Average Intentions (1-4)')
    # plt.xlabel('Typologies 1 to 4')
    # plt.ylabel('Number of Intentions')
    # plt.title('Number of Intentions by Typology (1 to 4)')
    # plt.xticks(rotation=45)
    # plt.tight_layout()
    # plt.show()

    # plt.figure(figsize=(10, 6))
    # plt.bar(typologies_5_to_8, average_intentions_5_to_8, label='Average Intentions (5-8)')
    # plt.xlabel('Typologies 5 to 8')
    # plt.ylabel('Number of Intentions')
    # plt.title('Number of Intentions by Typology (5 to 8)')
    # plt.xticks(rotation=45)
    # plt.tight_layout()
    # plt.show()



    # Prepare data for the bar chart
    data_1_to_4 = {
        'Typology': typologies_1_to_4,
        'Average Executable Intentions': [averages['average_intentions_executable_at_experiment_end'] for typology, averages in typology_averages.items() if int(typology.split('/')[-1]) in range(1, 5)],
        'Average Intentions Generated Correctly': [averages['average_intentions_generated_correctly'] for typology, averages in typology_averages.items() if int(typology.split('/')[-1]) in range(1, 5)]
    }

    data_5_to_8 = {
        'Typology': typologies_5_to_8,
        'Average Executable Intentions': [averages['average_intentions_executable_at_experiment_end'] for typology, averages in typology_averages.items() if int(typology.split('/')[-1]) in range(5, 9)],
        'Average Intentions Generated Correctly': [averages['average_intentions_generated_correctly'] for typology, averages in typology_averages.items() if int(typology.split('/')[-1]) in range(5, 9)]
    }

    # tab:green : #2ca02c
    # tab:red : #d62728
    plt.close()
    # Plot data for typologies 1 to 4
    plt.rc('font', size=15)
    plt.rc('axes', axisbelow=True)
    plt.figure(figsize=(9, 6))
    bar_width = 0.35
    index = range(len(data_1_to_4['Typology']))

    plt.bar(index, [float(elem) for elem in data_1_to_4['Average Intentions Generated Correctly']], bar_width, label='Intentions generated correctly', color=('#2ca02c', 0.3), edgecolor='black')
    plt.bar([i + bar_width for i in index], [float(elem) for elem in data_1_to_4['Average Executable Intentions']], bar_width, label='Intentions executable at experiment end', color = 'tab:green', edgecolor='black', hatch='/')

    plt.xlabel('Typologies 1 to 4')
    plt.ylabel('Fraction of Intentions')
    plt.xticks([i + bar_width / 2 for i in index], [int(elem) for elem in data_1_to_4['Typology']])
    plt.legend()
    plt.ylim(0, 1)
    plt.tight_layout()
    # plt.show()
    plt.savefig('/Users/francesco/Desktop/Master-Thesis/images/intentions_gen_vs_end_1_4.png', dpi=400)

    # Plot data for typologies 5 to 8
    plt.rc('font', size=15)
    plt.rc('axes', axisbelow=True)
    plt.figure(figsize=(9, 6))
    bar_width = 0.35
    index = range(len(data_5_to_8['Typology']))

    plt.bar(index, [float(elem) for elem in data_5_to_8['Average Intentions Generated Correctly']], bar_width, label='Intentions generated correctly', color=('#2ca02c', 0.3), edgecolor='black')
    plt.bar([i + bar_width for i in index], [float(elem) for elem in data_5_to_8['Average Executable Intentions']], bar_width, label='Intentions executable at experiment end', color = 'tab:green', edgecolor='black', hatch='/')

    plt.xlabel('Typologies 5 to 8')
    plt.ylabel('Fraction of Intentions')
    plt.xticks([i + bar_width / 2 for i in index], [int(elem) for elem in data_5_to_8['Typology']])
    plt.legend()
    plt.ylim(0, 1)
    plt.tight_layout()
    # plt.show()
    plt.savefig('/Users/francesco/Desktop/Master-Thesis/images/intentions_gen_vs_end_5_8.png', dpi=400)


    typologies = [typology.split('/')[-1] for typology in generation_failure_by_typology.keys()]
    execution_errors = [generation_failure_by_typology[typology]['execution_error'] for typology in generation_failure_by_typology.keys()]
    negative_evaluations = [generation_failure_by_typology[typology]['negative_evaluation'] for typology in generation_failure_by_typology.keys()]

    # plt.figure(figsize=(12, 6))
    # index = range(len(typologies))

    # plt.bar(index, execution_errors, label='Execution Error', color='red')
    # plt.bar(index, negative_evaluations, bottom=execution_errors, label='Negative Evaluation', color='orange')

    # plt.xlabel('Typologies')
    # plt.ylabel('Number of Intentions')
    # plt.title('Intentions Generation Failures by Typology')
    # plt.xticks(index, typologies, rotation=45)
    # plt.legend()
    # plt.tight_layout()
    # plt.show()




    # Prepare data for the bar chart
    typologies = [elem.split('/')[-1] for elem in typology_averages.keys()]
    average_execution_errors = [averages['average_intentions_generation_execution_error'] for typology, averages in typology_averages.items()]
    average_negative_evaluations = [averages['average_intentions_generation_negative_evaluation'] for typology, averages in typology_averages.items()]

    # Normalize the values so that for each typology the two bars sum to 1
    total_failures = [execution_error + negative_evaluation for execution_error, negative_evaluation in zip(average_execution_errors, average_negative_evaluations)]
    normalized_execution_errors = [execution_error / total if total != 0 else 0 for execution_error, total in zip(average_execution_errors, total_failures)]
    normalized_negative_evaluations = [negative_evaluation / total if total != 0 else 0 for negative_evaluation, total in zip(average_negative_evaluations, total_failures)]

    # Plot the data with bars on top of each other
    plt.rc('font', size=15)
    plt.rc('axes', axisbelow=True)
    plt.figure(figsize=(9, 6))
    bar_width = 0.70
    index = range(len(typologies))

    plt.bar(index, normalized_execution_errors, label='Execution Error', color='tab:orange', width=bar_width, edgecolor='black')
    plt.bar(index, normalized_negative_evaluations, bottom=normalized_execution_errors, label='Negative Evaluation', color='tab:olive', width=bar_width, edgecolor='black')

    plt.xlabel('Typology')
    plt.ylabel('Fraction of Intentions')
    plt.xticks(index, typologies)
    plt.legend()
    plt.ylim(0, 1)
    plt.tight_layout()
    # plt.show()
    plt.savefig('/Users/francesco/Desktop/Master-Thesis/images/intentions_failure_reasons.png', dpi=400)
