def function_6(event, belief_set):
    if event['object_type'] == 'parcel':
        if event['event_type'] == 'object added':
            if 'parcels' not in belief_set:
                belief_set['parcels'] = []
            belief_set['parcels'].append(event['object'])
        elif event['event_type'] == 'object changed':
            for parcel in belief_set['parcels']:
                if parcel['id'] == event['object']['id']:
                    parcel.update(event['object'])
        elif event['event_type'] == 'object removed':
            belief_set['parcels'] = [parcel for parcel in belief_set[
                'parcels'] if parcel['id'] != event['object']['id']]
    return belief_set
