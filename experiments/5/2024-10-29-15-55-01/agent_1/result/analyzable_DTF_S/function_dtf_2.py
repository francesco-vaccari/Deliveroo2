def function_dtf_2(belief_set):
    agent = belief_set['agent'][1]
    parcels = belief_set['parcels']
    map_grid = belief_set['map']['grid']
    walkable_cells = [cell for cell in map_grid if cell['cell_type'] ==
        'walkable' or cell['cell_type'] == 'parcels_spawn' or cell[
        'cell_type'] == 'delivery_cell']
    if len(walkable_cells) == 0 or len(parcels) == 0:
        return False
    if agent['score'] < 0:
        return False
    if len(agent['parcels_carried_ids']) > 0:
        return True
    return any(cell['cell_type'] == 'parcels_spawn' for cell in walkable_cells)
