def function_7():
    global belief_set
    parcel_spawn = [cell for cell in belief_set['map']['grid'] if cell[
        'cell_type'] == 'parcels_spawn'][0]['cell_coordinates']
    agent_pos = belief_set['agent']['coordinates']
    while agent_pos[0] > parcel_spawn[0]:
        function_1()
        agent_pos[0] -= 1
    while agent_pos[0] < parcel_spawn[0]:
        function_2()
        agent_pos[0] += 1
    while agent_pos[1] > parcel_spawn[1]:
        function_3()
        agent_pos[1] -= 1
    while agent_pos[1] < parcel_spawn[1]:
        function_4()
        agent_pos[1] += 1
    function_5()
