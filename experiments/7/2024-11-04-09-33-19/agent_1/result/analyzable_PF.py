def function_1(event, belief_set):
    if event['object_type'] == 'map':
        if event['event_type'] == 'object added':
            belief_set['map'] = event['object']
        elif event['event_type'] == 'object changed':
            for key, value in event['object'].items():
                belief_set['map'][key] = value
        elif event['event_type'] == 'object removed':
            del belief_set['map']
    return belief_set


def function_2(event, belief_set):
    if event['object_type'] == 'agent':
        if event['event_type'] == 'object added':
            belief_set['agent'] = event['object']
        elif event['event_type'] == 'object changed':
            belief_set['agent'].update(event['object'])
        elif event['event_type'] == 'object removed':
            del belief_set['agent']
    return belief_set


def function_3(event, belief_set):
    if event['object_type'] == 'key':
        if event['event_type'] == 'object added':
            if 'keys' not in belief_set:
                belief_set['keys'] = []
            belief_set['keys'].append(event['object'])
        elif event['event_type'] == 'object changed':
            for key in belief_set['keys']:
                if key['id'] == event['object']['id']:
                    key.update(event['object'])
        elif event['event_type'] == 'object removed':
            belief_set['keys'] = [key for key in belief_set['keys'] if key[
                'id'] != event['object']['id']]
    return belief_set


def function_4(event, belief_set):
    if event['object_type'] == 'door':
        if event['event_type'] == 'object added':
            if 'doors' not in belief_set:
                belief_set['doors'] = []
            belief_set['doors'].append(event['object'])
        elif event['event_type'] == 'object changed':
            for door in belief_set['doors']:
                if door['id'] == event['object']['id']:
                    door.update(event['object'])
        elif event['event_type'] == 'object removed':
            belief_set['doors'] = [door for door in belief_set['doors'] if 
                door['id'] != event['object']['id']]
    return belief_set


def function_5(event, belief_set):
    if event['object_type'] != 'battery':
        return belief_set
    if event['event_type'] == 'object added':
        if 'batteries' not in belief_set:
            belief_set['batteries'] = []
        belief_set['batteries'].append(event['object'])
    elif event['event_type'] == 'object changed':
        for i, battery in enumerate(belief_set.get('batteries', [])):
            if battery['id'] == event['object']['id']:
                belief_set['batteries'][i] = event['object']
                break
    elif event['event_type'] == 'object removed':
        belief_set['batteries'] = [battery for battery in belief_set.get(
            'batteries', []) if battery['id'] != event['object']['id']]
    return belief_set


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


