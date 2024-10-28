def function_2(event, belief_set):
    if event['object_type'] != 'parcel':
        return belief_set
    if event['event_type'] == 'object added':
        if 'parcels' not in belief_set:
            belief_set['parcels'] = {}
        belief_set['parcels'][event['object']['id']] = event['object']
    elif event['event_type'] == 'object changed':
        if 'parcels' not in belief_set or event['object']['id'
            ] not in belief_set['parcels']:
            return belief_set
        belief_set['parcels'][event['object']['id']].update(event['object'])
    elif event['event_type'] == 'object removed':
        if 'parcels' not in belief_set or event['object']['id'
            ] not in belief_set['parcels']:
            return belief_set
        del belief_set['parcels'][event['object']['id']]
    return belief_set
