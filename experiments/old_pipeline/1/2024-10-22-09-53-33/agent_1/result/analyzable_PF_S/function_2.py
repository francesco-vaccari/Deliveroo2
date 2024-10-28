def function_2(event, belief_set):
    if 'parcel' not in belief_set:
        belief_set['parcel'] = {}
    if event['event_type'] == 'object added' or event['event_type'
        ] == 'object changed':
        belief_set['parcel'][event['object']['id']] = event['object']
    elif event['event_type'] == 'object removed':
        if event['object']['id'] in belief_set['parcel']:
            del belief_set['parcel'][event['object']['id']]
    return belief_set
