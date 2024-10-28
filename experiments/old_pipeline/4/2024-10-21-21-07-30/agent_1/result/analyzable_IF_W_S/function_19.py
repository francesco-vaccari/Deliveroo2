def function_19():
    global belief_set
    agent = belief_set['agent']
    parcel = belief_set['parcel'][1]
    map = belief_set['map']['grid']
    delivery_cells = [cell for cell in map if cell['cell_type'] in [
        'delivery_cell', 'double_delivery_cell']]
    target_cell = min(delivery_cells, key=lambda cell: abs(cell[
        'cell_coordinates'][0] - agent['coordinates'][0]) + abs(cell[
        'cell_coordinates'][1] - agent['coordinates'][1]))
    if target_cell['cell_coordinates'][0] > agent['coordinates'][0]:
        function_2()
    elif target_cell['cell_coordinates'][0] < agent['coordinates'][0]:
        function_1()
    elif target_cell['cell_coordinates'][1] > agent['coordinates'][1]:
        function_4()
    elif target_cell['cell_coordinates'][1] < agent['coordinates'][1]:
        function_3()
    elif parcel['id'] in agent['parcels_carried_ids']:
        function_6()
