def function_1(event, belief_set):
    if event['object_type'] == 'map':
        if event['event_type'] == 'object added':
            belief_set['map'] = event['object']
        elif event['event_type'] == 'object changed':
            for cell in event['object']['grid']:
                for belief_cell in belief_set['map']['grid']:
                    if belief_cell['cell_coordinates'] == cell[
                        'cell_coordinates']:
                        belief_cell['cell_type'] = cell['cell_type']
                        break
        elif event['event_type'] == 'object removed':
            del belief_set['map']
    return belief_set
