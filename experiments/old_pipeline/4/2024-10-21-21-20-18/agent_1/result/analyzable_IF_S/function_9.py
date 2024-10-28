def function_9():
    global belief_set
    agent = belief_set['agent']
    parcels = belief_set['parcel']
    delivery_cells = [cell for cell in belief_set['map']['grid'] if 
        'delivery' in cell['cell_type']]
    for parcel in parcels.values():
        if parcel['carried_by_id'] is None and parcel['coordinates'] != agent[
            'coordinates']:
            if parcel['coordinates'][0] < agent['coordinates'][0]:
                function_1()
            elif parcel['coordinates'][0] > agent['coordinates'][0]:
                function_2()
            elif parcel['coordinates'][1] < agent['coordinates'][1]:
                function_3()
            elif parcel['coordinates'][1] > agent['coordinates'][1]:
                function_4()
        elif parcel['carried_by_id'] == agent['id']:
            nearest_delivery_cell = min(delivery_cells, key=lambda cell: 
                abs(cell['cell_coordinates'][0] - agent['coordinates'][0]) +
                abs(cell['cell_coordinates'][1] - agent['coordinates'][1]))
            if nearest_delivery_cell['cell_coordinates'][0] < agent[
                'coordinates'][0]:
                function_1()
            elif nearest_delivery_cell['cell_coordinates'][0] > agent[
                'coordinates'][0]:
                function_2()
            elif nearest_delivery_cell['cell_coordinates'][1] < agent[
                'coordinates'][1]:
                function_3()
            elif nearest_delivery_cell['cell_coordinates'][1] > agent[
                'coordinates'][1]:
                function_4()
        function_5() if parcel['coordinates'] == agent['coordinates'
            ] and parcel['carried_by_id'] is None else function_6(
            ) if nearest_delivery_cell['cell_coordinates'] == agent[
            'coordinates'] else None
