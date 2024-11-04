def function_8():
    global belief_set
    agent_id = 1
    agent_position = belief_set['agent'][agent_id]['coordinates']
    parcels = [parcel for parcel in belief_set['parcels'] if parcel[
        'carried_by_id'] == None and parcel['coordinates'] == agent_position]
    if parcels:
        function_5()
    else:
        function_7()
