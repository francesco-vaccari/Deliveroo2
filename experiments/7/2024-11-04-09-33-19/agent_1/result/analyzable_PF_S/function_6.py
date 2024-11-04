def function_6(event, belief_set):
    if event['object_type'] == 'parcel':
        if event['event_type'] == 'object added':
            if 'parcels' not in belief_set.keys():
                belief_set['parcels'] = [event['object']]
            else:
                belief_set['parcels'].append(event['object'])
        elif event['event_type'] == 'object changed':
            for i, parcel in enumerate(belief_set['parcels']):
                if parcel['id'] == event['object']['id']:
                    belief_set['parcels'][i] = event['object']
        elif event['event_type'] == 'object removed':
            belief_set['parcels'] = [parcel for parcel in belief_set[
                'parcels'] if parcel['id'] != event['object']['id']]
    return belief_set
