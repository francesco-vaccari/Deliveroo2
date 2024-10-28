def function_7():
    global belief_set
    agent = belief_set['agent']
    key = belief_set['key'][1]
    door = belief_set['door'][1]
    while agent['coordinates'] != key['coordinates']:
        if agent['coordinates'][0] < key['coordinates'][0]:
            function_2()
        elif agent['coordinates'][0] > key['coordinates'][0]:
            function_1()
        elif agent['coordinates'][1] < key['coordinates'][1]:
            function_4()
        else:
            function_3()
    function_5()
    while agent['coordinates'] != door['coordinates']:
        if agent['coordinates'][0] < door['coordinates'][0]:
            function_2()
        elif agent['coordinates'][0] > door['coordinates'][0]:
            function_1()
        elif agent['coordinates'][1] < door['coordinates'][1]:
            function_4()
        else:
            function_3()
    function_5()

def function_8():
    global belief_set
    agent = belief_set['agent']
    parcel = belief_set['parcel']
    key = belief_set['key']
    for parcel_id, parcel_info in parcel.items():
        if parcel_info['coordinates'] == agent['coordinates']:
            function_5()
    for key_id, key_info in key.items():
        if key_info['coordinates'] == agent['coordinates']:
            function_5()

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

def function_11():
    global belief_set
    agent = belief_set['agent']
    grid = belief_set['map']['grid']
    delivery_cells = [cell for cell in grid if cell['cell_type'] in [
        'delivery_cell', 'double_delivery_cell']]
    for cell in delivery_cells:
        if cell['cell_coordinates'][0] > agent['coordinates'][0]:
            function_2()
        elif cell['cell_coordinates'][0] < agent['coordinates'][0]:
            function_1()
        elif cell['cell_coordinates'][1] > agent['coordinates'][1]:
            function_4()
        elif cell['cell_coordinates'][1] < agent['coordinates'][1]:
            function_3()
        else:
            function_6()

def function_12():
    global belief_set
    agent = belief_set['agent']
    parcels = belief_set['parcel']
    map_grid = belief_set['map']['grid']
    delivery_cells = [cell['cell_coordinates'] for cell in map_grid if cell
        ['cell_type'] in ['delivery_cell', 'double_delivery_cell']]
    min_distance = float('inf')
    nearest_delivery_cell = None
    for cell in delivery_cells:
        distance = abs(agent['coordinates'][0] - cell[0]) + abs(agent[
            'coordinates'][1] - cell[1])
        if distance < min_distance:
            min_distance = distance
            nearest_delivery_cell = cell
    while agent['coordinates'] != nearest_delivery_cell:
        if agent['coordinates'][0] < nearest_delivery_cell[0]:
            function_2()
        elif agent['coordinates'][0] > nearest_delivery_cell[0]:
            function_1()
        if agent['coordinates'][1] < nearest_delivery_cell[1]:
            function_4()
        elif agent['coordinates'][1] > nearest_delivery_cell[1]:
            function_3()
    function_6()

def function_13():
    global belief_set
    agent = belief_set['agent']
    parcel = belief_set['parcel'][1]
    if agent['coordinates'] == parcel['coordinates']:
        function_5()
    delivery_cells = [cell for cell in belief_set['map']['grid'] if cell[
        'cell_type'] in ['delivery_cell', 'double_delivery_cell']]
    for cell in delivery_cells:
        if agent['coordinates'][0] < cell['cell_coordinates'][0]:
            while agent['coordinates'][0] != cell['cell_coordinates'][0]:
                function_2()
        elif agent['coordinates'][0] > cell['cell_coordinates'][0]:
            while agent['coordinates'][0] != cell['cell_coordinates'][0]:
                function_1()
        if agent['coordinates'][1] < cell['cell_coordinates'][1]:
            while agent['coordinates'][1] != cell['cell_coordinates'][1]:
                function_4()
        elif agent['coordinates'][1] > cell['cell_coordinates'][1]:
            while agent['coordinates'][1] != cell['cell_coordinates'][1]:
                function_3()
    function_6()

