def function_dtf_1(belief_set):
    if belief_set['parcel'] and any(cell['cell_type'] == 'parcels_spawn' for
        cell in belief_set['map']['grid']):
        return True
    else:
        return False


