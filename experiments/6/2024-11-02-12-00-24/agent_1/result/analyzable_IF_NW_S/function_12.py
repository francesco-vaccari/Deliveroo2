def function_12():
    global belief_set
    parcels = belief_set['parcels']
    agent = belief_set['agent']
    delivery_cell_coords = [cell['cell_coordinates'] for cell in belief_set
        ['map']['grid'] if cell['cell_type'] == 'delivery_cell'][0]
    while True:
        if len(parcels) == 0 or agent['energy'] <= 0:
            break
        else:
            closest_parcel_coords = min(parcels.values(), key=lambda x: abs
                (x['coordinates'][0] - agent['coordinates'][0]) + abs(x[
                'coordinates'][1] - agent['coordinates'][1]))['coordinates']
            while agent['coordinates'] != closest_parcel_coords:
                if agent['coordinates'][0] < closest_parcel_coords[0]:
                    function_2()
                elif agent['coordinates'][0] > closest_parcel_coords[0]:
                    function_1()
                elif agent['coordinates'][1] < closest_parcel_coords[1]:
                    function_4()
                else:
                    function_3()
                agent['coordinates'] = closest_parcel_coords
            function_5()
            while agent['coordinates'] != delivery_cell_coords:
                if agent['coordinates'][0] < delivery_cell_coords[0]:
                    function_2()
                elif agent['coordinates'][0] > delivery_cell_coords[0]:
                    function_1()
                elif agent['coordinates'][1] < delivery_cell_coords[1]:
                    function_4()
                else:
                    function_3()
                agent['coordinates'] = delivery_cell_coords
            function_6()
            parcels = {k: v for k, v in parcels.items() if v[
                'carried_by_id'] is None}
    return
