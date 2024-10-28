def function_1(event, belief_set):
    if 'map' not in belief_set:
        belief_set['map'] = {}
    if event['event_type'] == 'object added':
        belief_set['map'].update(event['object'])
    elif event['event_type'] == 'object changed':
        for cell in event['object']['grid']:
            for b_cell in belief_set['map']['grid']:
                if b_cell['cell_coordinates'] == cell['cell_coordinates']:
                    b_cell.update(cell)
                    break
    elif event['event_type'] == 'object removed':
        belief_set['map'] = {}
    return belief_set
