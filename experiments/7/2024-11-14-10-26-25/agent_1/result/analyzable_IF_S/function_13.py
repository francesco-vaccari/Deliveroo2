def function_13():
    global belief_set
    parcel_spawn_location = [cell['cell_coordinates'] for cell in
        belief_set['map']['grid'] if cell['cell_type'] == 'parcels_spawn'][0]
    agent_location = belief_set['agent']['coordinates']
    while agent_location != parcel_spawn_location:
        if agent_location[0] < parcel_spawn_location[0]:
            function_2()
        elif agent_location[0] > parcel_spawn_location[0]:
            function_1()
        elif agent_location[1] < parcel_spawn_location[1]:
            function_4()
        else:
            function_3()
        agent_location = belief_set['agent']['coordinates']
    function_5()
    if belief_set['agent']['energy'] < 30:
        battery_spawn_location = [cell['cell_coordinates'] for cell in
            belief_set['map']['grid'] if cell['cell_type'] == 'batteries_spawn'
            ][0]
        while agent_location != battery_spawn_location:
            if agent_location[0] < battery_spawn_location[0]:
                function_2()
            elif agent_location[0] > battery_spawn_location[0]:
                function_1()
            elif agent_location[1] < battery_spawn_location[1]:
                function_4()
            else:
                function_3()
            agent_location = belief_set['agent']['coordinates']
        function_5()
