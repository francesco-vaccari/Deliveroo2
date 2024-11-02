def function_3(event, belief_set):
    event_type = event['event_type']
    object_type = event['object_type']
    if object_type == 'parcel':
        if 'parcels' not in belief_set.keys():
            belief_set['parcels'] = {}
        if event_type == 'object added':
            belief_set['parcels'][event['object']['id']] = event['object']
        elif event_type == 'object changed':
            belief_set['parcels'][event['object']['id']].update(event['object']
                )
        elif event_type == 'object removed':
            belief_set['parcels'].pop(event['object']['id'], None)
    return belief_set
