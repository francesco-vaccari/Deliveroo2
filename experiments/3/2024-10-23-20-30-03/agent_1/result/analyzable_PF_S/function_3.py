def function_3(event, belief_set):
    if event['object_type'] == 'agent':
        agent = event['object']
        if event['event_type'] == 'object added':
            if 'agents' not in belief_set:
                belief_set['agents'] = {}
            belief_set['agents'][agent['id']] = agent
        elif event['event_type'] == 'object changed':
            if 'agents' in belief_set and agent['id'] in belief_set['agents']:
                belief_set['agents'][agent['id']].update(agent)
        elif event['event_type'] == 'object removed':
            if 'agents' in belief_set and agent['id'] in belief_set['agents']:
                del belief_set['agents'][agent['id']]
    return belief_set
