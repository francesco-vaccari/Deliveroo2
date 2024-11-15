def function_16():
    global belief_set
    agent = belief_set['agent'][1]
    locations = {'parcels_spawn': [], 'batteries_spawn': [],
        'delivery_cell': []}
    for cell in belief_set['map']['grid']:
        if cell['cell_type'] in locations:
            locations[cell['cell_type']].append(cell['cell_coordinates'])
    for location in locations.values():
        if location:
            closest = min(location, key=lambda x: abs(x[0] - agent[
                'coordinates'][0]) + abs(x[1] - agent['coordinates'][1]))
            if closest[0] < agent['coordinates'][0]:
                function_1()
            elif closest[0] > agent['coordinates'][0]:
                function_2()
            elif closest[1] < agent['coordinates'][1]:
                function_3()
            elif closest[1] > agent['coordinates'][1]:
                function_4()
