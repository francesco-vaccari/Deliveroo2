def function_12():
    global belief_set
    agent = belief_set['agent'][1]
    spawn_point = [item for item in belief_set['map']['grid'] if item[
        'cell_type'] == 'parcels_spawn'][0]['cell_coordinates']
    delivery_point = [item for item in belief_set['map']['grid'] if item[
        'cell_type'] == 'delivery_cell'][0]['cell_coordinates']
    previous_coordinates = agent['coordinates'][:]
    while True:
        if agent['coordinates'] == spawn_point:
            function_5()
        elif agent['coordinates'] == delivery_point:
            function_6()
        elif agent['coordinates'][0] > spawn_point[0]:
            function_1()
        elif agent['coordinates'][0] < spawn_point[0]:
            function_2()
        elif agent['coordinates'][1] > spawn_point[1]:
            function_3()
        elif agent['coordinates'][1] < spawn_point[1]:
            function_4()
        if previous_coordinates == agent['coordinates']:
            break
        else:
            previous_coordinates = agent['coordinates'][:]
