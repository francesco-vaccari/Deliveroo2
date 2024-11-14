def function_6(event, belief_set):
    if event['object_type'] == 'parcel':
        if event['event_type'] == 'object added':
            if 'parcels' in belief_set:
                belief_set['parcels'].append(event['object'])
            else:
                belief_set['parcels'] = [event['object']]
        elif event['event_type'] == 'object changed':
            parcels = belief_set.get('parcels', [])
            for i, parcel in enumerate(parcels):
                if parcel['id'] == event['object']['id']:
                    parcels[i] = event['object']
                    break
        elif event['event_type'] == 'object removed':
            parcels = belief_set.get('parcels', [])
            parcels = [parcel for parcel in parcels if parcel['id'] !=
                event['object']['id']]
            belief_set['parcels'] = parcels
    return belief_set
