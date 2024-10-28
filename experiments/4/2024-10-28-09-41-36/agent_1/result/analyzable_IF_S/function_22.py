def function_22():
    global belief_set
    agent_position = belief_set['agent']['coordinates']
    parcel_position = sorted(belief_set['parcels'].values(), key=lambda x: 
        abs(x['coordinates'][0] - agent_position[0]) + abs(x['coordinates']
        [1] - agent_position[1]))[0]['coordinates']
    while agent_position != parcel_position and len(belief_set['agent'][
        'parcels_carried_ids']) == 0:
        if agent_position[0] < parcel_position[0]:
            function_2()
        elif agent_position[0] > parcel_position[0]:
            function_1()
        elif agent_position[1] < parcel_position[1]:
            function_4()
        elif agent_position[1] > parcel_position[1]:
            function_3()
        agent_position = belief_set['agent']['coordinates']
        if agent_position == parcel_position:
            function_5()
            break
