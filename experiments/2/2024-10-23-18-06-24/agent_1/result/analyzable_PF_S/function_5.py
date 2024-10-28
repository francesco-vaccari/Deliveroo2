def function_5(event, belief_set):
    if 'door' in belief_set.keys():
        doors = belief_set['door']
    else:
        doors = {}
    if event['event_type'] == 'object added':
        doors[event['object']['id']] = event['object']
        belief_set['door'] = doors
    elif event['event_type'] == 'object changed':
        if event['object']['id'] in doors.keys():
            doors[event['object']['id']] = event['object']
            belief_set['door'] = doors
    elif event['event_type'] == 'object removed':
        if event['object']['id'] in doors.keys():
            del doors[event['object']['id']]
            belief_set['door'] = doors
    return belief_set
