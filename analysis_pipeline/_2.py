import matplotlib.pyplot as plt
import numpy as np

def _2(data):
    return
    n_desires = 0
    total_satisfied_with_trigger_executable_at_end = 0
    total_satisfied_with_trigger_not_executable_at_end = 0
    total_satisfied_without_trigger = 0
    total_not_satisfied = 0

    triggers = []
    
    for typology, experiments in data.items():
        satisfied_with_trigger_executable_at_end = 0
        satisfied_with_trigger_not_executable_at_end = 0
        satisfied_without_trigger = 0
        not_satisfied = 0
        for experiment in experiments:
            experiment_satisfied_with_trigger_executable_at_end = 0
            experiment_satisfied_with_trigger_not_executable_at_end = 0
            experiment_satisfied_without_trigger = 0
            experiment_not_satisfied = 0
            for desire_id, desire in experiment['desires'].items():
                n_desires += 1
                if desire['satisfied']:
                    if desire['trigger_function'] is None:
                        experiment_satisfied_without_trigger += 1
                    if desire['trigger_function'] is not None and desire['executable']:
                        experiment_satisfied_with_trigger_executable_at_end += 1
                    if desire['trigger_function'] is not None and not desire['executable']:
                        experiment_satisfied_with_trigger_not_executable_at_end += 1
                        temp = []
                        for evaluation in desire['evaluations']:
                            if evaluation:
                                temp.append('positive')
                            else:
                                if desire['error']:
                                    temp.append('error')
                                else:
                                    temp.append('negative')
                        triggers.append({
                            'typology': typology.split('/')[-1],
                            'desire_id': desire_id,
                            'experiment': experiment['path'],
                            'n': desire['triggered_n_times'],
                            'result': temp,
                        })
                if not desire['satisfied']:
                    experiment_not_satisfied += 1
            # print(f"Experiment {experiment['path']}:")
            # print(f"experiment_satisfied_with_trigger_executable_at_end: {experiment_satisfied_with_trigger_executable_at_end}")
            # print(f"experiment_satisfied_with_trigger_not_executable_at_end: {experiment_satisfied_with_trigger_not_executable_at_end}")
            # print(f"experiment_satisfied_without_trigger: {experiment_satisfied_without_trigger}")
            # print(f"experiment_not_satisfied: {experiment_not_satisfied}")
            # print()
            
            satisfied_with_trigger_executable_at_end += experiment_satisfied_with_trigger_executable_at_end
            satisfied_with_trigger_not_executable_at_end += experiment_satisfied_with_trigger_not_executable_at_end
            satisfied_without_trigger += experiment_satisfied_without_trigger
            not_satisfied += experiment_not_satisfied

        print(f"Typology {typology}:")
        print(f"satisfied_with_trigger_executable_at_end: {satisfied_with_trigger_executable_at_end}")
        print(f"satisfied_with_trigger_not_executable_at_end: {satisfied_with_trigger_not_executable_at_end}")
        print(f"satisfied_without_trigger: {satisfied_without_trigger}")
        print(f"not_satisfied: {not_satisfied}")
        print()

        total_satisfied_with_trigger_executable_at_end += satisfied_with_trigger_executable_at_end
        total_satisfied_with_trigger_not_executable_at_end += satisfied_with_trigger_not_executable_at_end
        total_satisfied_without_trigger += satisfied_without_trigger
        total_not_satisfied += not_satisfied

    print(f"Total:")
    print(f"total_satisfied_with_trigger_executable_at_end: {total_satisfied_with_trigger_executable_at_end}")
    print(f"total_satisfied_with_trigger_not_executable_at_end: {total_satisfied_with_trigger_not_executable_at_end}")
    print(f"total_satisfied_without_trigger: {total_satisfied_without_trigger}")
    print(f"total_not_satisfied: {total_not_satisfied}")
    print()

    print(f"Total n desires: {n_desires}")

    print("12 desires in total invalidated, 7 during their triggered execution")
    print("all desires except one had a runtime error in accessing belief set with wrong key")
    print("the remaining desire had a timeout error due to agent not having key to go through door and thus being stuck on moving action")

    
# error while accessing belief set, wrong key to read from 'keys' field
# same
# same
# did not pick up key to go through door
# same but batteris
# same but keys
# same but parcels

# A desire could have also been invalidated if the agent runs out of energy during desire triggered execution, but did not happen.

# 12 total invalidated desires, 7 during desire triggered execution


# Desires invalidated:
# experiments/6/2024-11-02-12-00-24/agent_1/control_manager.log
# experiments/6/2024-11-02-12-16-06/agent_1/control_manager.log
# experiments/6/2024-11-02-12-16-06/agent_1/control_manager.log
# experiments/8/2024-11-08-10-51-41/agent_1/control_manager.log
# experiments/8/2024-11-08-10-51-41/agent_1/control_manager.log
# experiments/8/2024-11-08-17-40-54/agent_1/control_manager.log
# experiments/8/2024-11-08-17-40-54/agent_1/control_manager.log
# experiments/8/2024-11-07-18-30-26/agent_1/control_manager.log
# experiments/8/2024-11-07-18-30-26/agent_1/control_manager.log
# experiments/8/2024-11-07-18-30-26/agent_1/control_manager.log
# experiments/5/2024-10-29-15-55-01/agent_1/control_manager.log
# experiments/5/2024-11-01-09-48-01/agent_1/control_manager.log

# Invalidate after trigger execution:
# experiments/6/2024-11-02-12-16-06/agent_1/control_manager.log
# experiments/8/2024-11-08-10-51-41/agent_1/control_manager.log
# experiments/8/2024-11-08-17-40-54/agent_1/control_manager.log
# experiments/8/2024-11-07-18-30-26/agent_1/control_manager.log
# experiments/8/2024-11-07-18-30-26/agent_1/control_manager.log
# experiments/8/2024-11-07-18-30-26/agent_1/control_manager.log
# experiments/5/2024-10-29-15-55-01/agent_1/control_manager.log


    print('----------------------------------------------------------')
    desires_judged_as_satisfied_rate = (total_satisfied_with_trigger_executable_at_end + total_satisfied_with_trigger_not_executable_at_end + total_satisfied_without_trigger) / n_desires
    print(f"Desires judged by LLM as satisfied: {desires_judged_as_satisfied_rate}")
    desires_satisfied_no_trigger_rate = total_satisfied_without_trigger / n_desires
    print(f"Desires judged as satisfied but trigger function generation failed: {desires_satisfied_no_trigger_rate}")
    desires_correctly_generated_rate = (total_satisfied_with_trigger_executable_at_end + total_satisfied_with_trigger_not_executable_at_end) / n_desires
    print(f"Desires correctly generated: {desires_correctly_generated_rate}")
    desires_then_invalidated = total_satisfied_with_trigger_not_executable_at_end / n_desires
    print(f"Desires correctly generated but later invalidated: {desires_then_invalidated}")
    print('----------------------------------------------------------')





    # for elem in triggers:
    #     print(f"Typology: {elem['typology']}")
    #     print(f"n: {elem['n']}")
    #     print(f"result: {elem['result']}")
    #     print()

    typologies = []
    experiment_name = set()
    experiment_n = 0

    for typology, experiments in data.items():
        experiment_name = set()
        experiment_n = 0
        typology = {'name': typology.split('/')[-1], 
                    'satisfied': 0,
                    'not_satisfied': 0,
                    'satisfied_with_trigger': 0,
                    'satisfied_without_trigger': 0,
                    'satisfied_with_trigger_triggered': 0,
                    'satisfied_with_trigger_not_triggered': 0,
                    'satisfied_with_trigger_triggered_still_triggerable': 0,
                    'satisfied_with_trigger_triggered_not_triggerable': 0,
                    'desires_triggered': []
                    }

        for experiment in experiments:
            for desire_id, desire in experiment['desires'].items():
                if desire['satisfied']:
                    typology['satisfied'] += 1
                else:
                    typology['not_satisfied'] += 1
                
                if desire['satisfied']:
                    if desire['trigger_function'] is None:
                        typology['satisfied_without_trigger'] += 1
                    else:
                        typology['satisfied_with_trigger'] += 1
                
                if desire['satisfied'] and desire['trigger_function'] is not None:
                    if desire['triggered_n_times'] > 0:
                        typology['satisfied_with_trigger_triggered'] += 1
                        if experiment['path'] not in experiment_name:
                            experiment_name.add(experiment['path'])
                            experiment_n += 1
                        typology['desires_triggered'].append({
                            'typology': typology['name'],
                            'desire_id': desire_id,
                            'experiment': experiment_n,
                            'n_triggers': desire['triggered_n_times'],
                            'results': desire['evaluations'],
                        })
                    else:
                        typology['satisfied_with_trigger_not_triggered'] += 1
                
                if desire['satisfied'] and desire['trigger_function'] is not None and desire['triggered_n_times'] > 0:
                    if desire['executable']:
                        typology['satisfied_with_trigger_triggered_still_triggerable'] += 1
                    else:
                        typology['satisfied_with_trigger_triggered_not_triggerable'] += 1
                
        typologies.append(typology)
        
    for typology in typologies:
        print(f"Typology: {typology['name']}")
        # print(f"Total satisfied with trigger and triggered and still triggerable: {typology['satisfied_with_trigger_triggered_still_triggerable']}")
        # print(f"Total satisfied with trigger and triggered and not triggerable: {typology['satisfied_with_trigger_triggered_not_triggerable']}")
        for desire in typology['desires_triggered']:
            print(f"Desire {desire['desire_id']} {desire['experiment']} triggered {desire['n_triggers']} times with results: {desire['results']}")
        print()

    import matplotlib.pyplot as plt
    import numpy as np

    categories = [
    'satisfied',
    'not_satisfied',
    'satisfied_with_trigger',
    'satisfied_without_trigger',
    'satisfied_with_trigger_triggered',
    'satisfied_with_trigger_not_triggered',
    'satisfied_with_trigger_triggered_still_triggerable',
    'satisfied_with_trigger_triggered_not_triggerable'
    ]

    typology_names = [typology['name'] for typology in typologies]
    satisfied_counts = [typology['satisfied'] for typology in typologies]
    not_satisfied_counts = [typology['not_satisfied'] for typology in typologies]
    satisfied_with_trigger_counts = [typology['satisfied_with_trigger'] for typology in typologies]
    satisfied_without_trigger_counts = [typology['satisfied_without_trigger'] for typology in typologies]
    satisfied_with_trigger_triggered_counts = [typology['satisfied_with_trigger_triggered'] for typology in typologies]
    satisfied_with_trigger_not_triggered_counts = [typology['satisfied_with_trigger_not_triggered'] for typology in typologies]
    satisfied_with_trigger_triggered_still_triggerable_counts = [typology['satisfied_with_trigger_triggered_still_triggerable'] for typology in typologies]
    satisfied_with_trigger_triggered_not_triggerable_counts = [typology['satisfied_with_trigger_triggered_not_triggerable'] for typology in typologies]

    x = np.arange(len(typology_names))

    bar_width = 0.15
    plt.rc('font', size=15)
    plt.rc('axes', axisbelow=True)
    plt.figure(figsize=(9, 6))
    plt.bar(x, satisfied_counts, bar_width, color=('#008000', 0.4), label='Satisfied', align='edge', edgecolor='black')
    plt.bar(x, not_satisfied_counts, bar_width, bottom=satisfied_counts, color=('#E50000', 0.4), label='Not Satisfied', align='edge', edgecolor='black')
    plt.bar(x + bar_width, satisfied_with_trigger_counts, bar_width, color=('#008000', 0.6), label='Triggerable', align='edge', edgecolor='black')
    plt.bar(x + bar_width, satisfied_without_trigger_counts, bar_width, color=('#E50000', 0.6), label='Not Triggerable', bottom=satisfied_with_trigger_counts, align='edge', edgecolor='black')
    plt.bar(x + 2*bar_width, satisfied_with_trigger_triggered_counts, bar_width, color=('#008000', 0.8), label='Triggered', align='edge', edgecolor='black')
    plt.bar(x + 2*bar_width, satisfied_with_trigger_not_triggered_counts, bar_width, color=('#E50000', 0.8), label='Untriggered', bottom=satisfied_with_trigger_triggered_counts, align='edge', edgecolor='black')
    plt.bar(x + 3*bar_width, satisfied_with_trigger_triggered_still_triggerable_counts, bar_width, color=('#008000', 1), label='Still Triggerable After', align='edge', edgecolor='black')
    plt.bar(x + 3*bar_width, satisfied_with_trigger_triggered_not_triggerable_counts, bar_width, color=('#E50000', 1), label='Not Triggerable After', bottom=satisfied_with_trigger_triggered_still_triggerable_counts, align='edge', edgecolor='black')

    plt.xlabel('Typology')
    plt.ylabel('Number of Desires')
    plt.xticks(x, typology_names)
    plt.yticks(np.arange(0, 28, 3))
    plt.grid(axis='y', linestyle='dashed')
    plt.legend()
    plt.tight_layout()
    # plt.show()
    plt.savefig('/Users/francesco/Desktop/Master-Thesis/images/n_desires_categories.png', dpi=400)




    # ora voglio mostrare il numero di trigger avvenuti in ogni categoria e se hanno funzionato o meno

    typology_names = [typology['name'] for typology in typologies][4:]
    positive_triggers_by_typology = [sum([sum([str(result) == 'True' for result in desire['results']]) for desire in typology['desires_triggered']]) for typology in typologies][4:]
    negative_triggers_by_typology = [sum([sum([str(result) == 'False' for result in desire['results']]) for desire in typology['desires_triggered']]) for typology in typologies][4:]
    n_triggers_by_typology = [sum([len(desire['results']) for desire in typology['desires_triggered']]) for typology in typologies][4:]

    bar_width = 0.3
    x = np.arange(5, 9)
    plt.rc('font', size=15)
    plt.rc('axes', axisbelow=True)
    plt.figure(figsize=(9, 6))
    
    # plt.bar(typology_names, n_triggers_by_typology, bar_width, label='Total', align='edge', edgecolor='black')

    trigger_error = [
        [1, 1],
        [1, 2],
        [0, 0],
        [5, 2]
    ]
    
    
    plt.bar(x, positive_triggers_by_typology, bar_width, color='green', label='Success', align='edge', edgecolor='black')
    plt.bar(x, negative_triggers_by_typology, bar_width, color='red', label='Failure', align='edge', bottom=positive_triggers_by_typology, edgecolor='black')
    plt.bar(x + bar_width/2, [elem[0] for elem in trigger_error], bar_width/2, color='orange', bottom=positive_triggers_by_typology, label='Execution Error', align='edge', edgecolor='black')
    plt.bar(x + bar_width/2, [elem[1] for elem in trigger_error], bar_width/2, color='yellow', bottom=[elem[0] + positive_triggers_by_typology[i] for i, elem in enumerate(trigger_error)], label='Negative Evaluation', align='edge', edgecolor='black')

    plt.xlabel('Typology')
    plt.ylabel('Number of Triggers')
    plt.xticks(x)
    plt.grid(axis='y', linestyle='dashed')
    plt.legend()
    plt.tight_layout()
    # plt.show()
    plt.savefig('/Users/francesco/Desktop/Master-Thesis/images/n_triggers.png', dpi=400)












    # import matplotlib.pyplot as plt

    # typologies = []
    # satisfied_with_trigger_executable_at_end_list = []
    # satisfied_with_trigger_not_executable_at_end_list = []
    # satisfied_without_trigger_list = []
    # not_satisfied_list = []

    # for typology, experiments in data.items():
    #     typologies.append(typology.split('/')[-1])
    #     satisfied_with_trigger_executable_at_end = 0
    #     satisfied_with_trigger_not_executable_at_end = 0
    #     satisfied_without_trigger = 0
    #     not_satisfied = 0
    #     for experiment in experiments:
    #         for desire_id, desire in experiment['desires'].items():
    #             if desire['satisfied']:
    #                 if desire['trigger_function'] is None:
    #                     satisfied_without_trigger += 1
    #                 if desire['trigger_function'] is not None and desire['executable']:
    #                     satisfied_with_trigger_executable_at_end += 1
    #                 if desire['trigger_function'] is not None and not desire['executable']:
    #                     satisfied_with_trigger_not_executable_at_end += 1
    #             if not desire['satisfied']:
    #                 not_satisfied += 1
    #     satisfied_with_trigger_executable_at_end_list.append(satisfied_with_trigger_executable_at_end)
    #     satisfied_with_trigger_not_executable_at_end_list.append(satisfied_with_trigger_not_executable_at_end)
    #     satisfied_without_trigger_list.append(satisfied_without_trigger)
    #     not_satisfied_list.append(not_satisfied)

    # x = range(len(typologies))

    # plt.figure(figsize=(10, 6))
    # plt.bar(x, satisfied_with_trigger_executable_at_end_list, width=0.5, label='Satisfied with trigger executable at end', align='center')
    # plt.bar(x, satisfied_with_trigger_not_executable_at_end_list, width=0.5, label='Satisfied with trigger not executable at end', align='center', bottom=satisfied_with_trigger_executable_at_end_list)
    # plt.bar(x, satisfied_without_trigger_list, width=0.5, label='Satisfied without trigger', align='center', bottom=[i+j for i,j in zip(satisfied_with_trigger_executable_at_end_list, satisfied_with_trigger_not_executable_at_end_list)])
    # plt.bar(x, not_satisfied_list, width=0.5, label='Not satisfied', align='center', bottom=[i+j+k for i,j,k in zip(satisfied_with_trigger_executable_at_end_list, satisfied_with_trigger_not_executable_at_end_list, satisfied_without_trigger_list)])

    # plt.xlabel('Typology')
    # plt.ylabel('Number of Desires')
    # plt.title('Desires Satisfaction by Typology')
    # plt.xticks(x, typologies, rotation='vertical')
    # plt.legend()
    # plt.tight_layout()
    # plt.show()



    # typologies = []
    # satisfied_with_trigger_executable_at_end_list = []
    # satisfied_with_trigger_not_executable_at_end_list = []
    # satisfied_without_trigger_list = []
    # not_satisfied_list = []

    # for typology, experiments in data.items():
    #     typologies.append(typology.split('/')[-1])
    #     satisfied_with_trigger_executable_at_end = 0
    #     satisfied_with_trigger_not_executable_at_end = 0
    #     satisfied_without_trigger = 0
    #     not_satisfied = 0
    #     total_desires = 0
    #     for experiment in experiments:
    #         for desire_id, desire in experiment['desires'].items():
    #             total_desires += 1
    #             if desire['satisfied']:
    #                 if desire['trigger_function'] is None:
    #                     satisfied_without_trigger += 1
    #                 if desire['trigger_function'] is not None and desire['executable']:
    #                     satisfied_with_trigger_executable_at_end += 1
    #                 if desire['trigger_function'] is not None and not desire['executable']:
    #                     satisfied_with_trigger_not_executable_at_end += 1
    #             if not desire['satisfied']:
    #                 not_satisfied += 1
    #     satisfied_with_trigger_executable_at_end_list.append(satisfied_with_trigger_executable_at_end / total_desires)
    #     satisfied_with_trigger_not_executable_at_end_list.append(satisfied_with_trigger_not_executable_at_end / total_desires)
    #     satisfied_without_trigger_list.append(satisfied_without_trigger / total_desires)
    #     not_satisfied_list.append(not_satisfied / total_desires)

    # x = range(len(typologies))

    # plt.figure(figsize=(10, 6))
    # plt.bar(x, satisfied_with_trigger_executable_at_end_list, width=0.5, label='Satisfied with trigger executable at end', align='center')
    # plt.bar(x, satisfied_with_trigger_not_executable_at_end_list, width=0.5, label='Satisfied with trigger not executable at end', align='center', bottom=satisfied_with_trigger_executable_at_end_list)
    # plt.bar(x, satisfied_without_trigger_list, width=0.5, label='Satisfied without trigger', align='center', bottom=[i+j for i,j in zip(satisfied_with_trigger_executable_at_end_list, satisfied_with_trigger_not_executable_at_end_list)])
    # plt.bar(x, not_satisfied_list, width=0.5, label='Not satisfied', align='center', bottom=[i+j+k for i,j,k in zip(satisfied_with_trigger_executable_at_end_list, satisfied_with_trigger_not_executable_at_end_list, satisfied_without_trigger_list)])

    # plt.xlabel('Typology')
    # plt.ylabel('Proportion of Desires')
    # plt.title('Desires Satisfaction by Typology')
    # plt.xticks(x, typologies, rotation='vertical')
    # plt.legend()
    # plt.tight_layout()
    # plt.show()



    # typologies = []
    # satisfied_with_trigger_executable_at_end_list = []
    # satisfied_with_trigger_not_executable_at_end_list = []
    # satisfied_without_trigger_list = []
    # not_satisfied_list = []

    # for typology, experiments in data.items():
    #     typologies.append(typology.split('/')[-1])
    #     satisfied_with_trigger_executable_at_end = 0
    #     satisfied_with_trigger_not_executable_at_end = 0
    #     satisfied_without_trigger = 0
    #     not_satisfied = 0
    #     for experiment in experiments:
    #         for desire_id, desire in experiment['desires'].items():
    #             if desire['satisfied']:
    #                 if desire['trigger_function'] is None:
    #                     satisfied_without_trigger += 1
    #                 if desire['trigger_function'] is not None and desire['executable']:
    #                     satisfied_with_trigger_executable_at_end += 1
    #                 if desire['trigger_function'] is not None and not desire['executable']:
    #                     satisfied_with_trigger_not_executable_at_end += 1
    #             if not desire['satisfied']:
    #                 not_satisfied += 1
    #     satisfied_with_trigger_executable_at_end_list.append(satisfied_with_trigger_executable_at_end)
    #     satisfied_with_trigger_not_executable_at_end_list.append(satisfied_with_trigger_not_executable_at_end)
    #     satisfied_without_trigger_list.append(satisfied_without_trigger)
    #     not_satisfied_list.append(not_satisfied)

    # x = range(len(typologies))

    # plt.figure(figsize=(10, 6))
    # plt.bar(x[:4], satisfied_with_trigger_executable_at_end_list[:4], width=0.5, label='Satisfied with trigger executable at end', align='center')
    # plt.bar(x[:4], satisfied_with_trigger_not_executable_at_end_list[:4], width=0.5, label='Satisfied with trigger not executable at end', align='center', bottom=satisfied_with_trigger_executable_at_end_list[:4])
    # plt.bar(x[:4], satisfied_without_trigger_list[:4], width=0.5, label='Satisfied without trigger', align='center', bottom=[i+j for i,j in zip(satisfied_with_trigger_executable_at_end_list[:4], satisfied_with_trigger_not_executable_at_end_list[:4])])
    # plt.bar(x[:4], not_satisfied_list[:4], width=0.5, label='Not satisfied', align='center', bottom=[i+j+k for i,j,k in zip(satisfied_with_trigger_executable_at_end_list[:4], satisfied_with_trigger_not_executable_at_end_list[:4], satisfied_without_trigger_list[:4])])

    # plt.xlabel('Typology')
    # plt.ylabel('Number of Desires')
    # plt.title('Desires Satisfaction by Typology (1-4)')
    # plt.xticks(x[:4], typologies[:4], rotation='vertical')
    # plt.legend()
    # plt.tight_layout()
    # plt.show()

    # plt.figure(figsize=(10, 6))
    # plt.bar(x[4:], satisfied_with_trigger_executable_at_end_list[4:], width=0.5, label='Satisfied with trigger executable at end', align='center')
    # plt.bar(x[4:], satisfied_with_trigger_not_executable_at_end_list[4:], width=0.5, label='Satisfied with trigger not executable at end', align='center', bottom=satisfied_with_trigger_executable_at_end_list[4:])
    # plt.bar(x[4:], satisfied_without_trigger_list[4:], width=0.5, label='Satisfied without trigger', align='center', bottom=[i+j for i,j in zip(satisfied_with_trigger_executable_at_end_list[4:], satisfied_with_trigger_not_executable_at_end_list[4:])])
    # plt.bar(x[4:], not_satisfied_list[4:], width=0.5, label='Not satisfied', align='center', bottom=[i+j+k for i,j,k in zip(satisfied_with_trigger_executable_at_end_list[4:], satisfied_with_trigger_not_executable_at_end_list[4:], satisfied_without_trigger_list[4:])])

    # plt.xlabel('Typology')
    # plt.ylabel('Number of Desires')
    # plt.title('Desires Satisfaction by Typology (5-8)')
    # plt.xticks(x[4:], typologies[4:], rotation='vertical')
    # plt.legend()
    # plt.tight_layout()
    # plt.show()

    # typologies = []
    # satisfied_with_trigger_executable_at_end_list = []
    # satisfied_with_trigger_not_executable_at_end_list = []
    # satisfied_without_trigger_list = []
    # not_satisfied_list = []

    # for typology, experiments in data.items():
    #     typologies.append(typology.split('/')[-1])
    #     satisfied_with_trigger_executable_at_end = 0
    #     satisfied_with_trigger_not_executable_at_end = 0
    #     satisfied_without_trigger = 0
    #     not_satisfied = 0
    #     total_desires = 0
    #     for experiment in experiments:
    #         for desire_id, desire in experiment['desires'].items():
    #             total_desires += 1
    #             if desire['satisfied']:
    #                 if desire['trigger_function'] is None:
    #                     satisfied_without_trigger += 1
    #                 if desire['trigger_function'] is not None and desire['executable']:
    #                     satisfied_with_trigger_executable_at_end += 1
    #                 if desire['trigger_function'] is not None and not desire['executable']:
    #                     satisfied_with_trigger_not_executable_at_end += 1
    #             if not desire['satisfied']:
    #                 not_satisfied += 1
    #     satisfied_with_trigger_executable_at_end_list.append(satisfied_with_trigger_executable_at_end / total_desires)
    #     satisfied_with_trigger_not_executable_at_end_list.append(satisfied_with_trigger_not_executable_at_end / total_desires)
    #     satisfied_without_trigger_list.append(satisfied_without_trigger / total_desires)
    #     not_satisfied_list.append(not_satisfied / total_desires)

    # x = range(len(typologies))

    # plt.figure(figsize=(10, 6))
    # plt.bar(x[:4], satisfied_with_trigger_executable_at_end_list[:4], width=0.5, label='Satisfied with trigger executable at end', align='center')
    # plt.bar(x[:4], satisfied_with_trigger_not_executable_at_end_list[:4], width=0.5, label='Satisfied with trigger not executable at end', align='center', bottom=satisfied_with_trigger_executable_at_end_list[:4])
    # plt.bar(x[:4], satisfied_without_trigger_list[:4], width=0.5, label='Satisfied without trigger', align='center', bottom=[i+j for i,j in zip(satisfied_with_trigger_executable_at_end_list[:4], satisfied_with_trigger_not_executable_at_end_list[:4])])
    # plt.bar(x[:4], not_satisfied_list[:4], width=0.5, label='Not satisfied', align='center', bottom=[i+j+k for i,j,k in zip(satisfied_with_trigger_executable_at_end_list[:4], satisfied_with_trigger_not_executable_at_end_list[:4], satisfied_without_trigger_list[:4])])

    # plt.xlabel('Typology')
    # plt.ylabel('Proportion of Desires')
    # plt.title('Desires Satisfaction by Typology (1-4)')
    # plt.xticks(x[:4], typologies[:4], rotation='vertical')
    # plt.legend()
    # plt.tight_layout()
    # plt.show()

    # plt.figure(figsize=(10, 6))
    # plt.bar(x[4:], satisfied_with_trigger_executable_at_end_list[4:], width=0.5, label='Satisfied with trigger executable at end', align='center')
    # plt.bar(x[4:], satisfied_with_trigger_not_executable_at_end_list[4:], width=0.5, label='Satisfied with trigger not executable at end', align='center', bottom=satisfied_with_trigger_executable_at_end_list[4:])
    # plt.bar(x[4:], satisfied_without_trigger_list[4:], width=0.5, label='Satisfied without trigger', align='center', bottom=[i+j for i,j in zip(satisfied_with_trigger_executable_at_end_list[4:], satisfied_with_trigger_not_executable_at_end_list[4:])])
    # plt.bar(x[4:], not_satisfied_list[4:], width=0.5, label='Not satisfied', align='center', bottom=[i+j+k for i,j,k in zip(satisfied_with_trigger_executable_at_end_list[4:], satisfied_with_trigger_not_executable_at_end_list[4:], satisfied_without_trigger_list[4:])])

    # plt.xlabel('Typology')
    # plt.ylabel('Proportion of Desires')
    # plt.title('Desires Satisfaction by Typology (5-8)')
    # plt.xticks(x[4:], typologies[4:], rotation='vertical')
    # plt.legend()
    # plt.tight_layout()
    # plt.show()



    for elem in triggers:
        print(f"Typology: {elem['typology']}")
        print(f"Desire: {elem['desire_id']}")
        print(f"Experiment: {elem['experiment']}")
        print(f"n: {elem['n']}")
        print(f"result: {elem['result']}")
        print()



    # typologies = list(set([trigger['typology'] for trigger in triggers]))
    # typologies.sort()

    # trigger_counts = {typology: {'positive': 0, 'negative': 0, 'error': 0} for typology in typologies}

    # for trigger in triggers:
    #     for result in trigger['result']:
    #         trigger_counts[trigger['typology']][result] += 1

    # x = range(len(typologies))

    # negative_counts = [trigger_counts[typology]['negative'] for typology in typologies]
    # error_counts = [trigger_counts[typology]['error'] for typology in typologies]

    # plt.figure(figsize=(10, 6))
    # plt.bar(x, negative_counts, width=0.5, label='Negative', align='center')
    # plt.bar(x, error_counts, width=0.5, label='Error', align='center', bottom=[i+j for i,j in zip(negative_counts, negative_counts)])

    # plt.xlabel('Typology')
    # plt.ylabel('Number of Triggers')
    # plt.title('Trigger Results by Typology')
    # plt.xticks(x, typologies, rotation='vertical')
    # plt.legend()
    # plt.tight_layout()
    # plt.show()


    # typologies = list(set([trigger['typology'] for trigger in triggers]))
    # typologies.sort()

    # trigger_counts = {typology: {'positive': 0, 'negative': 0, 'error': 0, 'total': 0} for typology in typologies}

    # for trigger in triggers:
    #     for result in trigger['result']:
    #         trigger_counts[trigger['typology']][result] += 1
    #         trigger_counts[trigger['typology']]['total'] += 1

    # x = range(len(typologies))

    # positive_counts = [trigger_counts[typology]['positive'] / trigger_counts[typology]['total'] for typology in typologies]
    # negative_counts = [trigger_counts[typology]['negative'] / trigger_counts[typology]['total'] for typology in typologies]
    # error_counts = [trigger_counts[typology]['error'] / trigger_counts[typology]['total'] for typology in typologies]

    # plt.figure(figsize=(10, 6))
    # plt.bar(x, positive_counts, width=0.5, label='Positive', align='center')
    # plt.bar(x, negative_counts, width=0.5, label='Negative', align='center', bottom=positive_counts)
    # plt.bar(x, error_counts, width=0.5, label='Error', align='center', bottom=[i+j for i,j in zip(positive_counts, negative_counts)])

    # plt.xlabel('Typology')
    # plt.ylabel('Proportion of Triggers')
    # plt.title('Normalized Trigger Results by Typology')
    # plt.xticks(x, typologies, rotation='vertical')
    # plt.legend()
    # plt.tight_layout()
    # plt.show()