def function_19():
    global belief_set
    delivered = False
    iterations = 0
    while not delivered and iterations < 50:
        agent_coords = belief_set['agent']['coordinates']
        delivery_coords = [cell['cell_coordinates'] for cell in belief_set[
            'map']['grid'] if cell['cell_type'] in ['delivery_cell',
            'double_points_delivery_cell']]
        for coords in delivery_coords:
            if agent_coords[0] < coords[0]:
                function_2()
            elif agent_coords[0] > coords[0]:
                function_1()
            elif agent_coords[1] < coords[1]:
                function_4()
            elif agent_coords[1] > coords[1]:
                function_3()
            else:
                function_6()
                delivered = True
                break
        iterations += 1
