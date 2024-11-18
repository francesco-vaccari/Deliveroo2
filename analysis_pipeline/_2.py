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
    import matplotlib.pyplot as plt

    typologies = []
    satisfied_with_trigger_executable_at_end_list = []
    satisfied_with_trigger_not_executable_at_end_list = []
    satisfied_without_trigger_list = []
    not_satisfied_list = []

    for typology, experiments in data.items():
        typologies.append(typology.split('/')[-1])
        satisfied_with_trigger_executable_at_end = 0
        satisfied_with_trigger_not_executable_at_end = 0
        satisfied_without_trigger = 0
        not_satisfied = 0
        for experiment in experiments:
            for desire_id, desire in experiment['desires'].items():
                if desire['satisfied']:
                    if desire['trigger_function'] is None:
                        satisfied_without_trigger += 1
                    if desire['trigger_function'] is not None and desire['executable']:
                        satisfied_with_trigger_executable_at_end += 1
                    if desire['trigger_function'] is not None and not desire['executable']:
                        satisfied_with_trigger_not_executable_at_end += 1
                if not desire['satisfied']:
                    not_satisfied += 1
        satisfied_with_trigger_executable_at_end_list.append(satisfied_with_trigger_executable_at_end)
        satisfied_with_trigger_not_executable_at_end_list.append(satisfied_with_trigger_not_executable_at_end)
        satisfied_without_trigger_list.append(satisfied_without_trigger)
        not_satisfied_list.append(not_satisfied)

    x = range(len(typologies))

    plt.figure(figsize=(10, 6))
    plt.bar(x, satisfied_with_trigger_executable_at_end_list, width=0.5, label='Satisfied with trigger executable at end', align='center')
    plt.bar(x, satisfied_with_trigger_not_executable_at_end_list, width=0.5, label='Satisfied with trigger not executable at end', align='center', bottom=satisfied_with_trigger_executable_at_end_list)
    plt.bar(x, satisfied_without_trigger_list, width=0.5, label='Satisfied without trigger', align='center', bottom=[i+j for i,j in zip(satisfied_with_trigger_executable_at_end_list, satisfied_with_trigger_not_executable_at_end_list)])
    plt.bar(x, not_satisfied_list, width=0.5, label='Not satisfied', align='center', bottom=[i+j+k for i,j,k in zip(satisfied_with_trigger_executable_at_end_list, satisfied_with_trigger_not_executable_at_end_list, satisfied_without_trigger_list)])

    plt.xlabel('Typology')
    plt.ylabel('Number of Desires')
    plt.title('Desires Satisfaction by Typology')
    plt.xticks(x, typologies, rotation='vertical')
    plt.legend()
    plt.tight_layout()
    plt.show()



    typologies = []
    satisfied_with_trigger_executable_at_end_list = []
    satisfied_with_trigger_not_executable_at_end_list = []
    satisfied_without_trigger_list = []
    not_satisfied_list = []

    for typology, experiments in data.items():
        typologies.append(typology.split('/')[-1])
        satisfied_with_trigger_executable_at_end = 0
        satisfied_with_trigger_not_executable_at_end = 0
        satisfied_without_trigger = 0
        not_satisfied = 0
        total_desires = 0
        for experiment in experiments:
            for desire_id, desire in experiment['desires'].items():
                total_desires += 1
                if desire['satisfied']:
                    if desire['trigger_function'] is None:
                        satisfied_without_trigger += 1
                    if desire['trigger_function'] is not None and desire['executable']:
                        satisfied_with_trigger_executable_at_end += 1
                    if desire['trigger_function'] is not None and not desire['executable']:
                        satisfied_with_trigger_not_executable_at_end += 1
                if not desire['satisfied']:
                    not_satisfied += 1
        satisfied_with_trigger_executable_at_end_list.append(satisfied_with_trigger_executable_at_end / total_desires)
        satisfied_with_trigger_not_executable_at_end_list.append(satisfied_with_trigger_not_executable_at_end / total_desires)
        satisfied_without_trigger_list.append(satisfied_without_trigger / total_desires)
        not_satisfied_list.append(not_satisfied / total_desires)

    x = range(len(typologies))

    plt.figure(figsize=(10, 6))
    plt.bar(x, satisfied_with_trigger_executable_at_end_list, width=0.5, label='Satisfied with trigger executable at end', align='center')
    plt.bar(x, satisfied_with_trigger_not_executable_at_end_list, width=0.5, label='Satisfied with trigger not executable at end', align='center', bottom=satisfied_with_trigger_executable_at_end_list)
    plt.bar(x, satisfied_without_trigger_list, width=0.5, label='Satisfied without trigger', align='center', bottom=[i+j for i,j in zip(satisfied_with_trigger_executable_at_end_list, satisfied_with_trigger_not_executable_at_end_list)])
    plt.bar(x, not_satisfied_list, width=0.5, label='Not satisfied', align='center', bottom=[i+j+k for i,j,k in zip(satisfied_with_trigger_executable_at_end_list, satisfied_with_trigger_not_executable_at_end_list, satisfied_without_trigger_list)])

    plt.xlabel('Typology')
    plt.ylabel('Proportion of Desires')
    plt.title('Desires Satisfaction by Typology')
    plt.xticks(x, typologies, rotation='vertical')
    plt.legend()
    plt.tight_layout()
    plt.show()



    typologies = []
    satisfied_with_trigger_executable_at_end_list = []
    satisfied_with_trigger_not_executable_at_end_list = []
    satisfied_without_trigger_list = []
    not_satisfied_list = []

    for typology, experiments in data.items():
        typologies.append(typology.split('/')[-1])
        satisfied_with_trigger_executable_at_end = 0
        satisfied_with_trigger_not_executable_at_end = 0
        satisfied_without_trigger = 0
        not_satisfied = 0
        for experiment in experiments:
            for desire_id, desire in experiment['desires'].items():
                if desire['satisfied']:
                    if desire['trigger_function'] is None:
                        satisfied_without_trigger += 1
                    if desire['trigger_function'] is not None and desire['executable']:
                        satisfied_with_trigger_executable_at_end += 1
                    if desire['trigger_function'] is not None and not desire['executable']:
                        satisfied_with_trigger_not_executable_at_end += 1
                if not desire['satisfied']:
                    not_satisfied += 1
        satisfied_with_trigger_executable_at_end_list.append(satisfied_with_trigger_executable_at_end)
        satisfied_with_trigger_not_executable_at_end_list.append(satisfied_with_trigger_not_executable_at_end)
        satisfied_without_trigger_list.append(satisfied_without_trigger)
        not_satisfied_list.append(not_satisfied)

    x = range(len(typologies))

    plt.figure(figsize=(10, 6))
    plt.bar(x[:4], satisfied_with_trigger_executable_at_end_list[:4], width=0.5, label='Satisfied with trigger executable at end', align='center')
    plt.bar(x[:4], satisfied_with_trigger_not_executable_at_end_list[:4], width=0.5, label='Satisfied with trigger not executable at end', align='center', bottom=satisfied_with_trigger_executable_at_end_list[:4])
    plt.bar(x[:4], satisfied_without_trigger_list[:4], width=0.5, label='Satisfied without trigger', align='center', bottom=[i+j for i,j in zip(satisfied_with_trigger_executable_at_end_list[:4], satisfied_with_trigger_not_executable_at_end_list[:4])])
    plt.bar(x[:4], not_satisfied_list[:4], width=0.5, label='Not satisfied', align='center', bottom=[i+j+k for i,j,k in zip(satisfied_with_trigger_executable_at_end_list[:4], satisfied_with_trigger_not_executable_at_end_list[:4], satisfied_without_trigger_list[:4])])

    plt.xlabel('Typology')
    plt.ylabel('Number of Desires')
    plt.title('Desires Satisfaction by Typology (1-4)')
    plt.xticks(x[:4], typologies[:4], rotation='vertical')
    plt.legend()
    plt.tight_layout()
    plt.show()

    plt.figure(figsize=(10, 6))
    plt.bar(x[4:], satisfied_with_trigger_executable_at_end_list[4:], width=0.5, label='Satisfied with trigger executable at end', align='center')
    plt.bar(x[4:], satisfied_with_trigger_not_executable_at_end_list[4:], width=0.5, label='Satisfied with trigger not executable at end', align='center', bottom=satisfied_with_trigger_executable_at_end_list[4:])
    plt.bar(x[4:], satisfied_without_trigger_list[4:], width=0.5, label='Satisfied without trigger', align='center', bottom=[i+j for i,j in zip(satisfied_with_trigger_executable_at_end_list[4:], satisfied_with_trigger_not_executable_at_end_list[4:])])
    plt.bar(x[4:], not_satisfied_list[4:], width=0.5, label='Not satisfied', align='center', bottom=[i+j+k for i,j,k in zip(satisfied_with_trigger_executable_at_end_list[4:], satisfied_with_trigger_not_executable_at_end_list[4:], satisfied_without_trigger_list[4:])])

    plt.xlabel('Typology')
    plt.ylabel('Number of Desires')
    plt.title('Desires Satisfaction by Typology (5-8)')
    plt.xticks(x[4:], typologies[4:], rotation='vertical')
    plt.legend()
    plt.tight_layout()
    plt.show()

    typologies = []
    satisfied_with_trigger_executable_at_end_list = []
    satisfied_with_trigger_not_executable_at_end_list = []
    satisfied_without_trigger_list = []
    not_satisfied_list = []

    for typology, experiments in data.items():
        typologies.append(typology.split('/')[-1])
        satisfied_with_trigger_executable_at_end = 0
        satisfied_with_trigger_not_executable_at_end = 0
        satisfied_without_trigger = 0
        not_satisfied = 0
        total_desires = 0
        for experiment in experiments:
            for desire_id, desire in experiment['desires'].items():
                total_desires += 1
                if desire['satisfied']:
                    if desire['trigger_function'] is None:
                        satisfied_without_trigger += 1
                    if desire['trigger_function'] is not None and desire['executable']:
                        satisfied_with_trigger_executable_at_end += 1
                    if desire['trigger_function'] is not None and not desire['executable']:
                        satisfied_with_trigger_not_executable_at_end += 1
                if not desire['satisfied']:
                    not_satisfied += 1
        satisfied_with_trigger_executable_at_end_list.append(satisfied_with_trigger_executable_at_end / total_desires)
        satisfied_with_trigger_not_executable_at_end_list.append(satisfied_with_trigger_not_executable_at_end / total_desires)
        satisfied_without_trigger_list.append(satisfied_without_trigger / total_desires)
        not_satisfied_list.append(not_satisfied / total_desires)

    x = range(len(typologies))

    plt.figure(figsize=(10, 6))
    plt.bar(x[:4], satisfied_with_trigger_executable_at_end_list[:4], width=0.5, label='Satisfied with trigger executable at end', align='center')
    plt.bar(x[:4], satisfied_with_trigger_not_executable_at_end_list[:4], width=0.5, label='Satisfied with trigger not executable at end', align='center', bottom=satisfied_with_trigger_executable_at_end_list[:4])
    plt.bar(x[:4], satisfied_without_trigger_list[:4], width=0.5, label='Satisfied without trigger', align='center', bottom=[i+j for i,j in zip(satisfied_with_trigger_executable_at_end_list[:4], satisfied_with_trigger_not_executable_at_end_list[:4])])
    plt.bar(x[:4], not_satisfied_list[:4], width=0.5, label='Not satisfied', align='center', bottom=[i+j+k for i,j,k in zip(satisfied_with_trigger_executable_at_end_list[:4], satisfied_with_trigger_not_executable_at_end_list[:4], satisfied_without_trigger_list[:4])])

    plt.xlabel('Typology')
    plt.ylabel('Proportion of Desires')
    plt.title('Desires Satisfaction by Typology (1-4)')
    plt.xticks(x[:4], typologies[:4], rotation='vertical')
    plt.legend()
    plt.tight_layout()
    plt.show()

    plt.figure(figsize=(10, 6))
    plt.bar(x[4:], satisfied_with_trigger_executable_at_end_list[4:], width=0.5, label='Satisfied with trigger executable at end', align='center')
    plt.bar(x[4:], satisfied_with_trigger_not_executable_at_end_list[4:], width=0.5, label='Satisfied with trigger not executable at end', align='center', bottom=satisfied_with_trigger_executable_at_end_list[4:])
    plt.bar(x[4:], satisfied_without_trigger_list[4:], width=0.5, label='Satisfied without trigger', align='center', bottom=[i+j for i,j in zip(satisfied_with_trigger_executable_at_end_list[4:], satisfied_with_trigger_not_executable_at_end_list[4:])])
    plt.bar(x[4:], not_satisfied_list[4:], width=0.5, label='Not satisfied', align='center', bottom=[i+j+k for i,j,k in zip(satisfied_with_trigger_executable_at_end_list[4:], satisfied_with_trigger_not_executable_at_end_list[4:], satisfied_without_trigger_list[4:])])

    plt.xlabel('Typology')
    plt.ylabel('Proportion of Desires')
    plt.title('Desires Satisfaction by Typology (5-8)')
    plt.xticks(x[4:], typologies[4:], rotation='vertical')
    plt.legend()
    plt.tight_layout()
    plt.show()



    # for elem in triggers:
    #     print(f"Typology: {elem['typology']}")
    #     print(f"n: {elem['n']}")
    #     print(f"result: {elem['result']}")
    #     print()



    typologies = list(set([trigger['typology'] for trigger in triggers]))
    typologies.sort()

    trigger_counts = {typology: {'positive': 0, 'negative': 0, 'error': 0} for typology in typologies}

    for trigger in triggers:
        for result in trigger['result']:
            trigger_counts[trigger['typology']][result] += 1

    x = range(len(typologies))

    positive_counts = [trigger_counts[typology]['positive'] for typology in typologies]
    negative_counts = [trigger_counts[typology]['negative'] for typology in typologies]
    error_counts = [trigger_counts[typology]['error'] for typology in typologies]

    plt.figure(figsize=(10, 6))
    plt.bar(x, positive_counts, width=0.5, label='Positive', align='center')
    plt.bar(x, negative_counts, width=0.5, label='Negative', align='center', bottom=positive_counts)
    plt.bar(x, error_counts, width=0.5, label='Error', align='center', bottom=[i+j for i,j in zip(positive_counts, negative_counts)])

    plt.xlabel('Typology')
    plt.ylabel('Number of Triggers')
    plt.title('Trigger Results by Typology')
    plt.xticks(x, typologies, rotation='vertical')
    plt.legend()
    plt.tight_layout()
    plt.show()


    typologies = list(set([trigger['typology'] for trigger in triggers]))
    typologies.sort()

    trigger_counts = {typology: {'positive': 0, 'negative': 0, 'error': 0, 'total': 0} for typology in typologies}

    for trigger in triggers:
        for result in trigger['result']:
            trigger_counts[trigger['typology']][result] += 1
            trigger_counts[trigger['typology']]['total'] += 1

    x = range(len(typologies))

    positive_counts = [trigger_counts[typology]['positive'] / trigger_counts[typology]['total'] for typology in typologies]
    negative_counts = [trigger_counts[typology]['negative'] / trigger_counts[typology]['total'] for typology in typologies]
    error_counts = [trigger_counts[typology]['error'] / trigger_counts[typology]['total'] for typology in typologies]

    plt.figure(figsize=(10, 6))
    plt.bar(x, positive_counts, width=0.5, label='Positive', align='center')
    plt.bar(x, negative_counts, width=0.5, label='Negative', align='center', bottom=positive_counts)
    plt.bar(x, error_counts, width=0.5, label='Error', align='center', bottom=[i+j for i,j in zip(positive_counts, negative_counts)])

    plt.xlabel('Typology')
    plt.ylabel('Proportion of Triggers')
    plt.title('Normalized Trigger Results by Typology')
    plt.xticks(x, typologies, rotation='vertical')
    plt.legend()
    plt.tight_layout()
    plt.show()