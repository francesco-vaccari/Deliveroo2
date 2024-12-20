def function_1(event, belief_set):
    if 'map' in event['object_type']:
        if event['event_type'] == 'object added':
            belief_set['map'] = event['object']
        elif event['event_type'] == 'object changed':
            for cell in event['object']['grid']:
                for existing_cell in belief_set['map']['grid']:
                    if existing_cell['cell_coordinates'] == cell[
                        'cell_coordinates']:
                        existing_cell['cell_type'] = cell['cell_type']
        elif event['event_type'] == 'object removed':
            del belief_set['map']
    return belief_set


def function_2(event, belief_set):
    if event['object_type'] == 'parcel':
        if event['event_type'] == 'object added':
            if 'parcels' not in belief_set:
                belief_set['parcels'] = {}
            belief_set['parcels'][event['object']['id']] = event['object']
        elif event['event_type'] == 'object changed':
            if 'parcels' in belief_set and event['object']['id'] in belief_set[
                'parcels']:
                belief_set['parcels'][event['object']['id']].update(event[
                    'object'])
        elif event['event_type'] == 'object removed':
            if 'parcels' in belief_set and event['object']['id'] in belief_set[
                'parcels']:
                del belief_set['parcels'][event['object']['id']]
    return belief_set


def function_3(event, belief_set):
    if event['object_type'] == 'agent':
        if event['event_type'] == 'object added':
            belief_set['agent'] = event['object']
        elif event['event_type'] == 'object changed':
            belief_set['agent'].update(event['object'])
        elif event['event_type'] == 'object removed':
            belief_set.pop('agent', None)
    return belief_set


def function_4(event, belief_set):
    if event['object_type'] == 'key':
        if event['event_type'] == 'object added':
            belief_set['keys'] = {event['object']['id']: event['object']}
        elif event['event_type'] == 'object changed':
            belief_set['keys'][event['object']['id']] = event['object']
        elif event['event_type'] == 'object removed':
            del belief_set['keys'][event['object']['id']]
    return belief_set


def function_5(event, belief_set):
    if event['object_type'] == 'door':
        if event['event_type'] == 'object added':
            if 'doors' not in belief_set:
                belief_set['doors'] = {}
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


