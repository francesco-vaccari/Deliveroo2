def function_13():
    global belief_set
    if belief_set['agent']['has_key']:
        for door in belief_set['doors'].values():
            if belief_set['agent']['coordinates'] == door['coordinates']:
                function_5()
    else:
        function_10()
    for parcel in belief_set['parcels'].values():
        if belief_set['agent']['coordinates'] == parcel['coordinates']:
            function_5()
    if belief_set['agent']['parcels_carried_ids']:
        function_11()
