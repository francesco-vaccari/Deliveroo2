def function_1():
    with open('agent_dir/functions/agent_1/plan.txt', 'a') as f:
        f.write('action_1\n')
        f.close()
    wait()


def function_2():
    with open('agent_dir/functions/agent_1/plan.txt', 'a') as f:
        f.write('action_2\n')
        f.close()
    wait()


def function_3():
    with open('agent_dir/functions/agent_1/plan.txt', 'a') as f:
        f.write('action_3\n')
        f.close()
    wait()


def function_4():
    with open('agent_dir/functions/agent_1/plan.txt', 'a') as f:
        f.write('action_4\n')
        f.close()
    wait()


def function_5():
    with open('agent_dir/functions/agent_1/plan.txt', 'a') as f:
        f.write('action_5\n')
        f.close()
    wait()


def function_6():
    with open('agent_dir/functions/agent_1/plan.txt', 'a') as f:
        f.write('action_6\n')
        f.close()
    wait()


def function_12():
    global belief_set
    if len(belief_set['agent'][1]['parcels_carried_ids']) > 0:
        for cell in belief_set['map']['map']['grid']:
            if cell['cell_type'] == 'delivery_cell' and cell['cell_coordinates'
                ] == belief_set['agent'][1]['coordinates']:
                function_6()
                break
        else:
            for cell in belief_set['map']['map']['grid']:
                if cell['cell_type'] == 'delivery_cell':
                    if cell['cell_coordinates'][0] < belief_set['agent'][1][
                        'coordinates'][0]:
                        function_1()
                    elif cell['cell_coordinates'][0] > belief_set['agent'][1][
                        'coordinates'][0]:
                        function_2()
                    elif cell['cell_coordinates'][1] < belief_set['agent'][1][
                        'coordinates'][1]:
                        function_3()
                    elif cell['cell_coordinates'][1] > belief_set['agent'][1][
                        'coordinates'][1]:
                        function_4()
                    break

