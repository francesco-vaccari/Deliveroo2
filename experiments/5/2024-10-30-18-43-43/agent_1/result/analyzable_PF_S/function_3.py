def function_3(event, belief_set):
    if event['object_type'] == 'parcel':
        if 'parcels' not in belief_set:
            belief_set['parcels'] = {}
        if event['event_type'] == 'object added':
            belief_set['parcels'][event['object']['id']] = event['object']
        elif event['event_type'] == 'object changed':
            belief_set['parcels'][event['object']['id']].update(event['object']
                )
        elif event['event_type'] == 'object removed':
            del belief_set['parcels'][event['object']['id']]
    return belief_set
