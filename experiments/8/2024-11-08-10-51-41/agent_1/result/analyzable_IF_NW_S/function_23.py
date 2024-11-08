def function_23():
    global belief_set
    agent = belief_set['agent'][1]
    if agent['energy'] < 30:
        function_16()
    else:
        function_14()
    if 'parcels' in belief_set and agent['coordinates'] in [parcel[
        'coordinates'] for parcel in belief_set['parcels'].values()]:
        function_5()
    if 'keys' in belief_set and agent['coordinates'] == belief_set['keys'][2][
        'coordinates']:
        function_5()
