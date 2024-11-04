def function_8():
    global belief_set
    parcels = belief_set['parcels']
    agent = belief_set['agent'][1]
    for parcel_id, parcel_info in parcels.items():
        if parcel_info['coordinates'] == agent['coordinates'] and parcel_info[
            'carried_by_id'] is None:
            function_5()
            break
