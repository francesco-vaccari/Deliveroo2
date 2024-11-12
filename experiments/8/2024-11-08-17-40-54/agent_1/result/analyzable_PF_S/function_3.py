def function_3(event, belief_set):
    if event['object_type'] != 'parcel':
        return belief_set
    if 'parcels' not in belief_set:
        belief_set['parcels'] = {}
    if event['event_type'] == 'object added':
        belief_set['parcels'][event['object']['id']] = event['object']
    elif event['event_type'] == 'object changed':
        if event['object']['id'] in belief_set['parcels']:
            belief_set['parcels'][event['object']['id']].update(event['object']
                )
    elif event['event_type'] == 'object removed':
        if event['object']['id'] in belief_set['parcels']:
            del belief_set['parcels'][event['object']['id']]
    return belief_set