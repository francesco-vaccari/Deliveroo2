def function_2(event, belief_set):
    object_type = event['object_type']
    event_type = event['event_type']
    object = event['object']
    if object_type == 'parcel':
        if event_type == 'object added':
            belief_set.setdefault(object_type, {})[object['id']] = object
        elif event_type == 'object changed':
            if object['id'] in belief_set.get(object_type, {}):
                belief_set[object_type][object['id']].update(object)
        elif event_type == 'object removed':
            if object['id'] in belief_set.get(object_type, {}):
                del belief_set[object_type][object['id']]
    return belief_set
