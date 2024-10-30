def function_dtf_1(belief_set):
    parcels_spawn_exists = any(cell['cell_type'] == 'parcels_spawn' for
        cell in belief_set['map']['grid'])
    delivery_cell_exists = any(cell['cell_type'] == 'delivery_cell' for
        cell in belief_set['map']['grid'])
    walkable_path_exists = any(cell['cell_type'] == 'walkable' for cell in
        belief_set['map']['grid'])
    parcels_exist = any(parcel['carried_by_id'] is None for parcel in
        belief_set['parcels'].values())
    agent_parcels = belief_set['agent'][1]['parcels_carried_ids']
    if (parcels_spawn_exists and delivery_cell_exists and
        walkable_path_exists and (parcels_exist or agent_parcels)):
        return True
    else:
        return False


