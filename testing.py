import json

response = """{"function": "def update_belief_set(event, belief_set):\n    object_type = event['object_type']\n    if object_type != 'agent':\n        return belief_set\n    \n    event_type = event['event_type']\n    obj = event['object']\n    obj_id = obj['id']\n    \n    if event_type == 'object added':\n        belief_set[obj_id] = obj\n    elif event_type == 'object changed':\n        if obj_id in belief_set:\n            belief_set[obj_id].update(obj)\n    elif event_type == 'object removed':\n        if obj_id in belief_set:\n            del belief_set[obj_id]\n    \n    return belief_set"}"""

response = response.replace("\n", "\\n")
response = response.replace("\t", "\\t")
response = json.loads(response)
# print(response['function'])


a = """{"function": "def update_belief_set(event, belief_set):\n    object_type = event['object_type']\n    if object_type != 'agent':\n        return belief_set\n    \n    event_type = event['event_type']\n    obj = event['object']\n    obj_id = obj['id']\n    \n    if event_type == 'object added':\n        belief_set[obj_id] = obj\n    elif event_type == 'object changed':\n        if obj_id in belief_set:\n            belief_set[obj_id].update(obj)\n    elif event_type == 'object removed':\n        if obj_id in belief_set:\n            del belief_set[obj_id]\n    \n    return belief_set"}"""


b = """{"function": "def update_belief_set(event, belief_set):\n    object_type = event['object_type']\n    if object_type != 'parcel':\n        return belief_set\n    \n    event_type = event['event_type']\n    obj = event['object']\n    obj_id = obj['id']\n    \n    if event_type == 'object added':\n        belief_set[obj_id] = obj\n    elif event_type == 'object changed':\n        if obj_id in belief_set:\n            belief_set[obj_id].update(obj)\n    elif event_type == 'object removed':\n        if obj_id in belief_set:\n            del belief_set[obj_id]\n    \n    return belief_set"}"""

a = a.replace("\n", "\\n")
a = a.replace("\t", "\\t")
b = b.replace("\n", "\\n")
b = b.replace("\t", "\\t")

a = json.loads(a)
b = json.loads(b)

print(a['function'])
print(b['function'])



def update_belief_set(event, belief_set):
    event_type = event['event_type']
    object_type = event['object_type']
    object_data = event['object']
    object_id = object_data['id']
    if object_type != 'parcel':
        return belief_set
    if event_type == 'object added':
        belief_set[object_id] = object_data
    elif event_type == 'object changed':
        if object_id in belief_set:
            belief_set[object_id].update(object_data)
    elif event_type == 'object removed':
        if object_id in belief_set:
            del belief_set[object_id]
    return belief_set

