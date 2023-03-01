def turn_right():
    turn_left()
    turn_left()
    turn_left()

def move_right():
    turn_right()
    move()

def find_open_path():
    while wall_in_front():
        turn_left()

def face_north():
    while not is_facing_north():
        turn_left()

def turn_around():
    turn_left()
    turn_left()

def all_is_clear():
    if wall_on_right() or wall_in_front():
        return False
    turn_around()
    if wall_on_right() or wall_in_front():
        turn_around()
        return False
    turn_around()
    return True

while not at_goal():
    if all_is_clear():
        face_north()
        move()
    elif right_is_clear():
        move_right()
    elif front_is_clear():
        move()
    else:
        turn_left()