def function_dtf_1(belief_set):
    if not belief_set['parcel']:
        return False
    agent_at_delivery = any(cell['cell_type'] in ['delivery_cell',
        'double_delivery_cell'] for cell in belief_set['map']['grid'] if 
        cell['cell_coordinates'] == belief_set['agent']['coordinates'])
    if agent_at_delivery and belief_set['agent']['parcels_carried_ids']:
        return True
    if not belief_set['agent']['parcels_carried_ids']:
        return True
    return False


