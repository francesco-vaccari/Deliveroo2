def function_7():
    global belief_set
    current_position = belief_set['agents'][1]['coordinates']
    parcel_position = belief_set['parcels'][1]['coordinates']
    if current_position[0] > parcel_position[0]:
        function_1()
    elif current_position[0] < parcel_position[0]:
        function_2()
    elif current_position[1] > parcel_position[1]:
        function_3()
    elif current_position[1] < parcel_position[1]:
        function_4()
    else:
        function_5()
