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


def function_7():
    global belief_set
    agent = belief_set['agent'][1]
    parcel = belief_set['parcel'][1]
    while agent['coordinates'] != parcel['coordinates']:
        if agent['coordinates'][0] > parcel['coordinates'][0]:
            function_1()
        elif agent['coordinates'][0] < parcel['coordinates'][0]:
            function_2()
        if agent['coordinates'][1] > parcel['coordinates'][1]:
            function_3()
        elif agent['coordinates'][1] < parcel['coordinates'][1]:
            function_4()
    function_5()

def function_8():
    global belief_set
    agent = belief_set['agent'][1]
    parcels = belief_set['parcel']
    map_grid = belief_set['map']['map']['grid']
    delivery_cell = [cell for cell in map_grid if cell['cell_type'] ==
        'delivery_cell'][0]['cell_coordinates']
    if agent['parcels_carried_ids']:
        if agent['coordinates'] == delivery_cell:
            function_6()
        elif agent['coordinates'][0] > delivery_cell[0]:
            function_1()
        elif agent['coordinates'][0] < delivery_cell[0]:
            function_2()
        elif agent['coordinates'][1] > delivery_cell[1]:
            function_3()
        elif agent['coordinates'][1] < delivery_cell[1]:
            function_4()
    else:
        for parcel in parcels.values():
            if agent['coordinates'] == parcel['coordinates']:
                function_5()
                break
            elif agent['coordinates'][0] > parcel['coordinates'][0]:
                function_1()
                break
            elif agent['coordinates'][0] < parcel['coordinates'][0]:
                function_2()
                break
            elif agent['coordinates'][1] > parcel['coordinates'][1]:
                function_3()
                break
            elif agent['coordinates'][1] < parcel['coordinates'][1]:
                function_4()
                break

def function_9():
    global belief_set
    agent = belief_set['agent'][1]
    delivery_cell = [cell for cell in belief_set['map']['map']['grid'] if 
        cell['cell_type'] == 'delivery_cell'][0]['cell_coordinates']
    if agent['coordinates'][0] < delivery_cell[0]:
        function_2()
    elif agent['coordinates'][0] > delivery_cell[0]:
        function_1()
    elif agent['coordinates'][1] < delivery_cell[1]:
        function_4()
    elif agent['coordinates'][1] > delivery_cell[1]:
        function_3()
    else:
        function_6()

def function_10():
    global belief_set
    agent = belief_set['agent'][1]
    parcels = belief_set['parcel']
    map_grid = belief_set['map']['map']['grid']
    delivery_cell = next(cell for cell in map_grid if cell['cell_type'] ==
        'delivery_cell')['cell_coordinates']
    while agent['coordinates'] != delivery_cell:
        if agent['coordinates'][0] < delivery_cell[0]:
            function_2()
        elif agent['coordinates'][0] > delivery_cell[0]:
            function_1()
        if agent['coordinates'][1] < delivery_cell[1]:
            function_4()
        elif agent['coordinates'][1] > delivery_cell[1]:
            function_3()
    function_6()

def function_11():
    global belief_set
    parcel_location = [p['coordinates'] for p in belief_set['parcel'].
        values() if p['carried_by_id'] is None][0]
    agent_location = belief_set['agent'][1]['coordinates']
    while agent_location != parcel_location:
        if agent_location[0] < parcel_location[0]:
            function_2()
        elif agent_location[0] > parcel_location[0]:
            function_1()
        elif agent_location[1] < parcel_location[1]:
            function_4()
        elif agent_location[1] > parcel_location[1]:
            function_3()
        agent_location = belief_set['agent'][1]['coordinates']
    function_5()
    delivery_location = [c['cell_coordinates'] for c in belief_set['map'][
        'map']['grid'] if c['cell_type'] == 'delivery_cell'][0]
    while agent_location != delivery_location:
        if agent_location[0] < delivery_location[0]:
            function_2()
        elif agent_location[0] > delivery_location[0]:
            function_1()
        elif agent_location[1] < delivery_location[1]:
            function_4()
        elif agent_location[1] > delivery_location[1]:
            function_3()
        agent_location = belief_set['agent'][1]['coordinates']
    function_6()

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

