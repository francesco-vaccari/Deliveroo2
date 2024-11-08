def function_27():
    global belief_set
    parcel_location = next((parcel['coordinates'] for parcel in belief_set[
        'parcels'].values() if parcel['carried_by_id'] is None), None)
    if belief_set['agent'][1]['coordinates'] == parcel_location:
        function_5()
    elif belief_set['agent'][1]['coordinates'][0] < parcel_location[0]:
        function_2()
    elif belief_set['agent'][1]['coordinates'][0] > parcel_location[0]:
        function_1()
    elif belief_set['agent'][1]['coordinates'][1] < parcel_location[1]:
        function_4()
    elif belief_set['agent'][1]['coordinates'][1] > parcel_location[1]:
        function_3()
    delivery_cell_location = next((cell['cell_coordinates'] for cell in
        belief_set['map']['grid'] if cell['cell_type'] == 'delivery_cell'),
        None)
    if belief_set['agent'][1]['coordinates'] == delivery_cell_location:
        function_6()
    elif belief_set['agent'][1]['coordinates'][0] < delivery_cell_location[0]:
        function_2()
    elif belief_set['agent'][1]['coordinates'][0] > delivery_cell_location[0]:
        function_1()
    elif belief_set['agent'][1]['coordinates'][1] < delivery_cell_location[1]:
        function_4()
    elif belief_set['agent'][1]['coordinates'][1] > delivery_cell_location[1]:
        function_3()
