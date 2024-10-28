def function_8():
    global belief_set
    agent = belief_set['agent']
    parcel = belief_set['parcel']
    key = belief_set['key']
    for parcel_id, parcel_info in parcel.items():
        if parcel_info['coordinates'] == agent['coordinates']:
            function_5()
    for key_id, key_info in key.items():
        if key_info['coordinates'] == agent['coordinates']:
            function_5()
