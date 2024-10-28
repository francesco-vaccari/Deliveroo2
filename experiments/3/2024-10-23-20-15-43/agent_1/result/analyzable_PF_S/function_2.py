def function_2(event, beliefs):
    if event['object_type'] == 'parcel':
        if event['event_type'] == 'object added':
            if 'parcels' not in beliefs:
                beliefs['parcels'] = {}
            beliefs['parcels'][event['object']['id']] = event['object']
        elif event['event_type'] == 'object changed':
            if 'parcels' in beliefs and event['object']['id'] in beliefs[
                'parcels']:
                beliefs['parcels'][event['object']['id']].update(event[
                    'object'])
        elif event['event_type'] == 'object removed':
            if 'parcels' in beliefs and event['object']['id'] in beliefs[
                'parcels']:
                del beliefs['parcels'][event['object']['id']]
    return beliefs
