def function_4(event, belief_set):
    if event['object_type'] != 'door':
        return belief_set
    if event['event_type'] == 'object added':
        if 'doors' not in belief_set:
            belief_set['doors'] = []
        belief_set['doors'].append(event['object'])
    elif event['event_type'] == 'object changed':
        for door in belief_set['doors']:
            if door['id'] == event['object']['id']:
                door.update(event['object'])
    elif event['event_type'] == 'object removed':
        belief_set['doors'] = [door for door in belief_set['doors'] if door
            ['id'] != event['object']['id']]
    return belief_set
