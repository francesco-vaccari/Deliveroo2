def function_4(event, belief_set):
    object_type = event['object_type']
    event_type = event['event_type']
    object = event['object']
    if object_type == 'key':
        if object_type not in belief_set:
            belief_set[object_type] = {}
        if event_type == 'object added':
            belief_set[object_type][object['id']] = object
        elif event_type == 'object changed':
            belief_set[object_type][object['id']].update(object)
        elif event_type == 'object removed':
            del belief_set[object_type][object['id']]
    return belief_set
