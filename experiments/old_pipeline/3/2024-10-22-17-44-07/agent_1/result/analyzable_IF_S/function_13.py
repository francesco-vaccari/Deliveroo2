def function_13():
    global belief_set
    agent_pos = belief_set['agent']['coordinates']
    parcels_carried = belief_set['agent']['parcels_carried_ids']
    if len(parcels_carried) > 0:
        for cell in belief_set['map']['grid']:
            if cell['cell_type'] in ['delivery_cell', 'double_delivery_cell'
                ] and cell['cell_coordinates'][0] > agent_pos[0]:
                function_2()
                break
            elif cell['cell_type'] in ['delivery_cell', 'double_delivery_cell'
                ] and cell['cell_coordinates'][0] < agent_pos[0]:
                function_1()
                break
            elif cell['cell_type'] in ['delivery_cell', 'double_delivery_cell'
                ] and cell['cell_coordinates'][1] > agent_pos[1]:
                function_4()
                break
            elif cell['cell_type'] in ['delivery_cell', 'double_delivery_cell'
                ] and cell['cell_coordinates'][1] < agent_pos[1]:
                function_3()
                break
        else:
            function_6()
    else:
        return
