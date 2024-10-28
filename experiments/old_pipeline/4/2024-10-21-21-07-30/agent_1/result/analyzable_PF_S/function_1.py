def function_1(event, belief_set):
    if 'map' not in belief_set:
        belief_set['map'] = {}
    if event['event_type'] == 'object added':
        belief_set['map'] = event['object']
    elif event['event_type'] == 'object changed':
        for cell in event['object']['grid']:
            for existing_cell in belief_set['map']['grid']:
                if existing_cell['cell_coordinates'] == cell['cell_coordinates'
                    ]:
                    existing_cell['cell_type'] = cell['cell_type']
    elif event['event_type'] == 'object removed':
        belief_set.pop('map', None)
    return belief_set
