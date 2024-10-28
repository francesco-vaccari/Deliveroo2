def function_12():
    global belief_set
    doors = belief_set['doors']
    agent = belief_set['agents'][1]
    min_distance = float('inf')
    nearest_door = None
    for door in doors.values():
        distance = abs(door['coordinates'][0] - agent['coordinates'][0]) + abs(
            door['coordinates'][1] - agent['coordinates'][1])
        if distance < min_distance:
            min_distance = distance
            nearest_door = door
    if nearest_door is not None:
        if nearest_door['coordinates'][0] < agent['coordinates'][0]:
            function_1()
        elif nearest_door['coordinates'][0] > agent['coordinates'][0]:
            function_2()
        if nearest_door['coordinates'][1] < agent['coordinates'][1]:
            function_3()
        elif nearest_door['coordinates'][1] > agent['coordinates'][1]:
            function_4()
