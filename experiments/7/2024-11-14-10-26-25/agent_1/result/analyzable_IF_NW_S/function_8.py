def function_8():
    global belief_set
    parcels = belief_set['parcels']
    agent = belief_set['agent']
    map_width = belief_set['map']['width']
    map_height = belief_set['map']['height']
    parcel_distances = [(abs(parcel['coordinates'][0] - agent['coordinates'
        ][0]) + abs(parcel['coordinates'][1] - agent['coordinates'][1]),
        parcel) for parcel in parcels if parcel['carried_by_id'] is None]
    parcel_distances.sort(key=lambda x: x[0])
    for distance, parcel in parcel_distances:
        dx = parcel['coordinates'][0] - agent['coordinates'][0]
        dy = parcel['coordinates'][1] - agent['coordinates'][1]
        while dx != 0 and 0 <= agent['coordinates'][0] + dx < map_width:
            if dx > 0:
                function_2()
                dx -= 1
            else:
                function_1()
                dx += 1
        while dy != 0 and 0 <= agent['coordinates'][1] + dy < map_height:
            if dy > 0:
                function_4()
                dy -= 1
            else:
                function_3()
                dy += 1
        if dx == 0 and dy == 0:
            function_5()
            return
