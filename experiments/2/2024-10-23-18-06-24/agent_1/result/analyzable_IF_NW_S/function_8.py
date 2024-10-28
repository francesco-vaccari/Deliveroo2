def function_8():
    global belief_set
    while belief_set['agent']['coordinates'][0] > belief_set['parcel'][1][
        'coordinates'][0]:
        function_1()
    while belief_set['agent']['coordinates'][0] < belief_set['parcel'][1][
        'coordinates'][0]:
        function_2()
    while belief_set['agent']['coordinates'][1] > belief_set['parcel'][1][
        'coordinates'][1]:
        function_3()
    while belief_set['agent']['coordinates'][1] < belief_set['parcel'][1][
        'coordinates'][1]:
        function_4()
    function_5()
    while belief_set['agent']['coordinates'][0] > belief_set['map']['grid'][7][
        'cell_coordinates'][0]:
        function_1()
    while belief_set['agent']['coordinates'][0] < belief_set['map']['grid'][7][
        'cell_coordinates'][0]:
        function_2()
    while belief_set['agent']['coordinates'][1] > belief_set['map']['grid'][7][
        'cell_coordinates'][1]:
        function_3()
    while belief_set['agent']['coordinates'][1] < belief_set['map']['grid'][7][
        'cell_coordinates'][1]:
        function_4()
    function_6()
