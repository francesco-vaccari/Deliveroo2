def function_13():
    global belief_set
    agent = belief_set['agent']
    batteries = belief_set['batteries']
    closest_battery = min(batteries, key=lambda battery: abs(battery[
        'coordinates'][0] - agent['coordinates'][0]) + abs(battery[
        'coordinates'][1] - agent['coordinates'][1]))
    while agent['coordinates'][0] < closest_battery['coordinates'][0]:
        function_2()
    while agent['coordinates'][0] > closest_battery['coordinates'][0]:
        function_1()
    while agent['coordinates'][1] < closest_battery['coordinates'][1]:
        function_4()
    while agent['coordinates'][1] > closest_battery['coordinates'][1]:
        function_3()
    function_5()
