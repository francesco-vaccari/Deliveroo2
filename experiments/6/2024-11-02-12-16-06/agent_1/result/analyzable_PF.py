def function_1(event, belief_set):
    if event['object_type'] == 'map':
        if event['event_type'] == 'object added':
            belief_set['map'] = event['object']
        elif event['event_type'] == 'object changed':
            for cell in event['object']['grid']:
                for belief_cell in belief_set['map']['grid']:
                    if belief_cell['cell_coordinates'] == cell[
                        'cell_coordinates']:
                        belief_cell['cell_type'] = cell['cell_type']
                        break
        elif event['event_type'] == 'object removed':
            del belief_set['map']
    return belief_set


def function_2(event, belief_set):
    if event['object_type'] == 'agent':
        if event['event_type'] == 'object added':
            belief_set['agent'] = {event['object']['id']: event['object']}
        elif event['event_type'] == 'object changed':
            belief_set['agent'][event['object']['id']].update(event['object'])
        elif event['event_type'] == 'object removed':
            del belief_set['agent'][event['object']['id']]
    return belief_set


def function_3(event, belief_set):
    if event['object_type'] != 'battery':
        return belief_set
    if 'batteries' not in belief_set:
        belief_set['batteries'] = {}
    if event['event_type'] == 'object added':
        belief_set['batteries'][event['object']['id']] = event['object']
    elif event['event_type'] == 'object changed':
        belief_set['batteries'][event['object']['id']] = event['object']
    elif event['event_type'] == 'object removed':
        del belief_set['batteries'][event['object']['id']]
    return belief_set


def function_4(event, belief_set):
    if event['object_type'] == 'parcel':
        if event['event_type'] == 'object added':
            if 'parcels' not in belief_set:
                belief_set['parcels'] = {}
            belief_set['parcels'][event['object']['id']] = event['object']
        elif event['event_type'] == 'object removed':
            if 'parcels' in belief_set and event['object']['id'] in belief_set[
                'parcels']:
                del belief_set['parcels'][event['object']['id']]
        elif event['event_type'] == 'object changed':
            if 'parcels' in belief_set and event['object']['id'] in belief_set[
                'parcels']:
                belief_set['parcels'][event['object']['id']] = event['object']
    return belief_set


