plan = []

def move_up(belief_set):
    global plan
    plan.append('moveup')

def move_down(belief_set):
    global plan
    plan.append('movedown')

def move_left(belief_set):
    global plan
    plan.append('moveleft')

def move_right(belief_set):
    global plan
    plan.append('moveright')

def pick_up(belief_set):
    global plan
    plan.append('pickup')

def put_down(belief_set):
    global plan
    plan.append('putdown')

def function_0(belief_set):
    move_up(belief_set)


def function_1(belief_set):
    move_down(belief_set)


