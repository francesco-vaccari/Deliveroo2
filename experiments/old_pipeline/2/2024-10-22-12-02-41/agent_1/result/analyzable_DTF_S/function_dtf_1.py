def function_dtf_1(belief_set):
    for key in belief_set['keys']:
        if belief_set['keys'][key]['carried_by_id'] is None:
            return True
    for cell in belief_set['map']['grid']:
        if cell['cell_type'] == 'walkable' and cell['cell_coordinates'
            ] != belief_set['agent']['coordinates']:
            return True
    return False
