def function_21():
    global belief_set
    delivery_cell = next(cell for cell in belief_set['map']['grid'] if cell
        ['cell_type'] == 'delivery_cell')
    agent = belief_set['agent'][1]
    dx, dy = delivery_cell['cell_coordinates'][0] - agent['coordinates'][0
        ], delivery_cell['cell_coordinates'][1] - agent['coordinates'][1]
    if dx < 0:
        function_1()
    elif dx > 0:
        function_2()
    elif dy < 0:
        function_3()
    elif dy > 0:
        function_4()
    function_6()
