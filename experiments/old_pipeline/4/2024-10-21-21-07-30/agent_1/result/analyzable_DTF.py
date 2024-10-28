def function_dtf_1(belief_set):
    if 'parcel' not in belief_set or not belief_set['parcel']:
        return False
    if 'agent' in belief_set and belief_set['agent']['id'] == 1 and belief_set[
        'agent']['parcels_carried_ids']:
        return True
    if 'key' in belief_set and belief_set['key'][1]['carried_by_id'] == 1:
        return True
    if 'door' in belief_set and any(door['id'] == 1 for door in belief_set[
        'door'].values() if door['coordinates'] == belief_set['agent'][
        'coordinates']):
        return True
    return False


