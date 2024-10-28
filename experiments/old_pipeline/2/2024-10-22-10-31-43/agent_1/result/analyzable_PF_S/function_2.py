def function_2(event, belief_set):
    object_type = event['object_type']
    if object_type == 'parcel':
        if event['event_type'] == 'object added':
            if object_type not in belief_set:
                belief_set[object_type] = {}
            belief_set[object_type][event['object']['id']] = event['object']
        elif event['event_type'] == 'object changed':
            if event['object']['id'] in belief_set[object_type]:
                belief_set[object_type][event['object']['id']].update(event
                    ['object'])
        elif event['event_type'] == 'object removed':
            if event['object']['id'] in belief_set[object_type]:
                del belief_set[object_type][event['object']['id']]
    return belief_set
