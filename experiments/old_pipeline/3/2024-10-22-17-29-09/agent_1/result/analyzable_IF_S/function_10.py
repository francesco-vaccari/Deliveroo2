def function_10():
    global belief_set
    agent = belief_set['agent']
    parcels = belief_set['parcel']
    map = belief_set['map']['grid']
    for parcel in parcels.values():
        if parcel['carried_by_id'] == agent['id']:
            for cell in map:
                if cell['cell_type'] in ['delivery_cell',
                    'double_delivery_cell'] and agent['coordinates'] != cell[
                    'cell_coordinates']:
                    if cell['cell_coordinates'][0] < agent['coordinates'][0]:
                        function_1()
                    elif cell['cell_coordinates'][0] > agent['coordinates'][0]:
                        function_2()
                    elif cell['cell_coordinates'][1] < agent['coordinates'][1]:
                        function_3()
                    elif cell['cell_coordinates'][1] > agent['coordinates'][1]:
                        function_4()
            if agent['coordinates'] == cell['cell_coordinates']:
                function_6()
                break
