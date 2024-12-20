def function_1(event, belief_set):
    if event['event_type'] == 'object added':
        belief_set[event['object_type']] = event['object']
    elif event['event_type'] == 'object changed':
        for key, value in event['object'].items():
            belief_set[event['object_type']][key] = value
    elif event['event_type'] == 'object removed':
        del belief_set[event['object_type']]
    return belief_set


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


def function_3(event, belief_set):
    if event['object_type'] == 'agent':
        id = event['object']['id']
        if event['event_type'] == 'object added':
            if 'agents' not in belief_set:
                belief_set['agents'] = {}
            belief_set['agents'][id] = event['object']
        elif event['event_type'] == 'object changed':
            if 'agents' in belief_set and id in belief_set['agents']:
                belief_set['agents'][id].update(event['object'])
        elif event['event_type'] == 'object removed':
            if 'agents' in belief_set and id in belief_set['agents']:
                del belief_set['agents'][id]
    return belief_set


def function_4(event, belief_set):
    if event['object_type'] == 'key':
        if event['event_type'] == 'object added':
            belief_set['keys'] = {event['object']['id']: event['object']}
        elif event['event_type'] == 'object changed':
            if 'keys' in belief_set and event['object']['id'] in belief_set[
                'keys']:
                belief_set['keys'][event['object']['id']].update(event[
                    'object'])
        elif event['event_type'] == 'object removed':
            if 'keys' in belief_set and event['object']['id'] in belief_set[
                'keys']:
                del belief_set['keys'][event['object']['id']]
    return belief_set


def function_5(event, belief_set):
    if event['object_type'] == 'door':
        if event['event_type'] == 'object added':
            belief_set['doors'] = belief_set.get('doors', {})
            belief_set['doors'][event['object']['id']] = event['object']
        elif event['event_type'] == 'object changed':
            if 'doors' in belief_set and event['object']['id'] in belief_set[
                'doors']:
                belief_set['doors'][event['object']['id']].update(event[
                    'object'])
        elif event['event_type'] == 'object removed':
            if 'doors' in belief_set and event['object']['id'] in belief_set[
                'doors']:
                del belief_set['doors'][event['object']['id']]
    return belief_set


