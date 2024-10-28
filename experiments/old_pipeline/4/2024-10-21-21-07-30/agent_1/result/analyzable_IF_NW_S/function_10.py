def function_10():
    global belief_set
    agent = belief_set['agent']
    parcel = belief_set['parcel'][1]
    if agent['coordinates'] == parcel['coordinates'] and 1 in agent[
        'parcels_carried_ids']:
        function_4()
    elif agent['has_key'] and belief_set['door'][1]['coordinates'] in [[
        agent['coordinates'][0] + 1, agent['coordinates'][1]], [agent[
        'coordinates'][0] - 1, agent['coordinates'][1]], [agent[
        'coordinates'][0], agent['coordinates'][1] - 1], [agent[
        'coordinates'][0], agent['coordinates'][1] + 1]]:
        function_5()
    elif agent['coordinates'] == belief_set['map']['grid'][3][
        'cell_coordinates'] and 1 in agent['parcels_carried_ids']:
        function_6()
    else:
        function_2()
        function_4()
