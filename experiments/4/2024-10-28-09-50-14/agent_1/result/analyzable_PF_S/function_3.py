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
