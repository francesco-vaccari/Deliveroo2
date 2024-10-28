def function_13():
    global belief_set
    agent = belief_set['agent']
    parcels = agent['parcels_carried_ids']
    if parcels and any(cell for cell in belief_set['map']['grid'] if cell[
        'cell_type'] in ['delivery_cell', 'double_points_delivery_cell'] and
        cell['cell_coordinates'] == agent['coordinates']):
        function_6()
    elif agent['coordinates'][0] < belief_set['map']['width'] - 1:
        function_2()
    elif agent['coordinates'][0] > 0:
        function_1()
    elif agent['coordinates'][1] < belief_set['map']['height'] - 1:
        function_4()
    elif agent['coordinates'][1] > 0:
        function_3()
