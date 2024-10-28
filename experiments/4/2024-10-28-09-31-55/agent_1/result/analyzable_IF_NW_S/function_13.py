def function_13():
    global belief_set
    agent = belief_set['agent']
    parcels = belief_set['parcels']
    map_ = belief_set['map']['grid']
    delivered = False
    while not delivered:
        if not agent['parcels_carried_ids']:
            function_8()
            if agent['coordinates'] == parcels[1]['coordinates']:
                function_5()
        else:
            delivery_cells = [cell['cell_coordinates'] for cell in map_ if 
                'delivery' in cell['cell_type']]
            nearest_delivery_cell = min(delivery_cells, key=lambda x: abs(x
                [0] - agent['coordinates'][0]) + abs(x[1] - agent[
                'coordinates'][1]))
            while agent['coordinates'] != nearest_delivery_cell:
                if agent['coordinates'][0] < nearest_delivery_cell[0]:
                    function_2()
                elif agent['coordinates'][0] > nearest_delivery_cell[0]:
                    function_1()
                elif agent['coordinates'][1] < nearest_delivery_cell[1]:
                    function_4()
                elif agent['coordinates'][1] > nearest_delivery_cell[1]:
                    function_3()
            function_6()
            delivered = True
