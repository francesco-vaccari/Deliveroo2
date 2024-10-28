def function_dtf_1(belief_set):
    if belief_set['parcels'] and not belief_set['agent']['parcels_carried_ids'
        ]:
        return True
    if belief_set['agent']['parcels_carried_ids']:
        delivery_cell = next((cell for cell in belief_set['map']['grid'] if
            cell['cell_type'] == 'delivery_cell'), None)
        if delivery_cell and belief_set['agent']['coordinates'
            ] != delivery_cell['cell_coordinates']:
            return True
    if belief_set['keys'] and not belief_set['agent']['has_key']:
        return True
    if belief_set['doors'] and belief_set['agent']['has_key']:
        return True
    return False
