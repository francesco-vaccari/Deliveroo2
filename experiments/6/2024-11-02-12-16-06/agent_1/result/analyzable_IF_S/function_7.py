def function_7():
    global belief_set
    agent = belief_set['agent'][1]
    if agent['energy'] < 50:
        battery_spawn = next(cell for cell in belief_set['map']['grid'] if 
            cell['cell_type'] == 'batteries_spawn')['cell_coordinates']
        if agent['coordinates'][0] > battery_spawn[0]:
            function_1()
        elif agent['coordinates'][0] < battery_spawn[0]:
            function_2()
        elif agent['coordinates'][1] > battery_spawn[1]:
            function_3()
        else:
            function_4()
    else:
        parcel_spawn = next(cell for cell in belief_set['map']['grid'] if 
            cell['cell_type'] == 'parcels_spawn')['cell_coordinates']
        if agent['coordinates'][0] > parcel_spawn[0]:
            function_1()
        elif agent['coordinates'][0] < parcel_spawn[0]:
            function_2()
        elif agent['coordinates'][1] > parcel_spawn[1]:
            function_3()
        else:
            function_4()
