def function_8():
    global belief_set
    spawn = [cell['cell_coordinates'] for cell in belief_set['map']['grid'] if
        cell['cell_type'] == 'parcels_spawn'][0]
    delivery = [cell['cell_coordinates'] for cell in belief_set['map'][
        'grid'] if cell['cell_type'] == 'delivery_cell'][0]
    agent = belief_set['agent']['coordinates']
    while agent != spawn:
        if agent[0] < spawn[0]:
            function_2()
        elif agent[0] > spawn[0]:
            function_1()
        elif agent[1] < spawn[1]:
            function_4()
        elif agent[1] > spawn[1]:
            function_3()
    function_5()
    while agent != delivery:
        if agent[0] < delivery[0]:
            function_2()
        elif agent[0] > delivery[0]:
            function_1()
        elif agent[1] < delivery[1]:
            function_4()
        elif agent[1] > delivery[1]:
            function_3()
    function_6()
