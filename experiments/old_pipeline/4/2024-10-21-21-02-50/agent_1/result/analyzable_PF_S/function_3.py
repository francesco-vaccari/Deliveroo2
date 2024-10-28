def function_3(event, belief_set):
    if event['object_type'] == 'agent':
        if event['event_type'] == 'object added':
            if 'agents' not in belief_set:
                belief_set['agents'] = {}
            belief_set['agents'][event['object']['id']] = event['object']
        elif event['event_type'] == 'object changed':
            if event['object']['id'] in belief_set['agents']:
                belief_set['agents'][event['object']['id']].update(event[
                    'object'])
        elif event['event_type'] == 'object removed':
            if event['object']['id'] in belief_set['agents']:
                del belief_set['agents'][event['object']['id']]
    return belief_set
