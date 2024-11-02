def function_15():
    global belief_set
    agent = belief_set['agent'][1]
    location = agent['coordinates']
    energy = agent['energy']
    if energy < 50:
        function_14()
    else:
        unexplored_cells = [cell for cell in belief_set['map']['grid'] if 
            cell['cell_type'] == 'walkable' and cell['cell_coordinates'] !=
            location]
        if unexplored_cells:
            nearest_cell = min(unexplored_cells, key=lambda cell: abs(cell[
                'cell_coordinates'][0] - location[0]) + abs(cell[
                'cell_coordinates'][1] - location[1]))
            while location != nearest_cell['cell_coordinates']:
                if nearest_cell['cell_coordinates'][0] < location[0]:
                    function_1()
                elif nearest_cell['cell_coordinates'][0] > location[0]:
                    function_2()
                elif nearest_cell['cell_coordinates'][1] < location[1]:
                    function_3()
                elif nearest_cell['cell_coordinates'][1] > location[1]:
                    function_4()
                location = belief_set['agent'][1]['coordinates']
