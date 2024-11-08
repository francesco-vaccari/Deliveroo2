def function_12():
    global belief_set
    agent_coords = belief_set['agent']['coordinates']
    battery_coords = list(belief_set['batteries'].values())[0]
    if agent_coords[0] < battery_coords[0]:
        function_2()
    elif agent_coords[0] > battery_coords[0]:
        function_1()
    elif agent_coords[1] < battery_coords[1]:
        function_4()
    elif agent_coords[1] > battery_coords[1]:
        function_3()
    else:
        function_5()
