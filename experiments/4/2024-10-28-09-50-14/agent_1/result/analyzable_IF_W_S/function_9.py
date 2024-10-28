def function_9():
    global belief_set
    agent = belief_set['agents'][1]
    if not agent['parcels_carried_ids']:
        parcel = min(belief_set['parcels'].values(), key=lambda p: abs(p[
            'coordinates'][0] - agent['coordinates'][0]) + abs(p[
            'coordinates'][1] - agent['coordinates'][1]))
        dx = parcel['coordinates'][0] - agent['coordinates'][0]
        dy = parcel['coordinates'][1] - agent['coordinates'][1]
        if dx > 0:
            function_2()
        elif dx < 0:
            function_1()
        elif dy > 0:
            function_4()
        elif dy < 0:
            function_3()
        if parcel['coordinates'] == agent['coordinates']:
            function_5()
