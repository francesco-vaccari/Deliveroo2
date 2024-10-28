def function_9():
    global belief_set
    agent = belief_set['agent']
    parcels = belief_set['parcel']
    for parcel in parcels.values():
        if parcel['coordinates'] == agent['coordinates'] and not agent[
            'parcels_carried_ids']:
            function_5()
            break
