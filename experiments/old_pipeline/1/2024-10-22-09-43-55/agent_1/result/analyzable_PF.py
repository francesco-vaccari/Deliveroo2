def function_1(event, belief_set):
    if 'map' not in belief_set:
        belief_set['map'] = {}
    if event['event_type'] == 'object added':
        belief_set['map'].update(event['object'])
    elif event['event_type'] == 'object changed':
        for cell in event['object']['grid']:
            for b_cell in belief_set['map']['grid']:
                if b_cell['cell_coordinates'] == cell['cell_coordinates']:
                    b_cell.update(cell)
                    break
    elif event['event_type'] == 'object removed':
        belief_set['map'] = {}
    return belief_set


def function_2(event, belief_set):
    if 'parcels' not in belief_set:
        belief_set['parcels'] = {}
    if event['event_type'] == 'object added':
        belief_set['parcels'][event['object']['id']] = event['object']
    elif event['event_type'] == 'object changed':
        belief_set['parcels'][event['object']['id']].update(event['object'])
    elif event['event_type'] == 'object removed':
        del belief_set['parcels'][event['object']['id']]
    return belief_set


def function_3(event, belief_set):
    if event['object_type'] == 'agent':
        if event['event_type'] == 'object added':
            belief_set['agent'] = event['object']
        elif event['event_type'] == 'object changed':
            belief_set['agent'].update(event['object'])
        elif event['event_type'] == 'object removed':
            del belief_set['agent']
    return belief_set


