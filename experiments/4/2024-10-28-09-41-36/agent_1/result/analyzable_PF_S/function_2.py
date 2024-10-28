def function_2(event, belief):
    if event['object_type'] == 'parcel':
        if event['event_type'] == 'object added':
            if 'parcels' not in belief:
                belief['parcels'] = {}
            belief['parcels'][event['object']['id']] = event['object']
        elif event['event_type'] == 'object changed':
            if 'parcels' in belief and event['object']['id'] in belief[
                'parcels']:
                belief['parcels'][event['object']['id']].update(event['object']
                    )
        elif event['event_type'] == 'object removed':
            if 'parcels' in belief and event['object']['id'] in belief[
                'parcels']:
                del belief['parcels'][event['object']['id']]
    return belief
