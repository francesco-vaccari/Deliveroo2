def function_7():
    global belief_set
    agent = belief_set['agent'][1]
    map = belief_set['map']['grid']
    unvisited_cells = [cell for cell in map if cell['cell_type'] in [
        'parcels_spawn', 'batteries_spawn', 'delivery_cell'] and cell[
        'cell_coordinates'] != agent['coordinates']]
    if not unvisited_cells:
        return
    nearest_cell = min(unvisited_cells, key=lambda cell: abs(cell[
        'cell_coordinates'][0] - agent['coordinates'][0]) + abs(cell[
        'cell_coordinates'][1] - agent['coordinates'][1]))
    if nearest_cell['cell_coordinates'][0] < agent['coordinates'][0]:
        function_1()
    elif nearest_cell['cell_coordinates'][0] > agent['coordinates'][0]:
        function_2()
    elif nearest_cell['cell_coordinates'][1] < agent['coordinates'][1]:
        function_3()
    elif nearest_cell['cell_coordinates'][1] > agent['coordinates'][1]:
        function_4()
