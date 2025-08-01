import random
from moves import apply_moves


def scramble(cube, count = 20):
    moves = ["U", "U'", "D", "D'", "L", "L'", "R", "R'", "F", "F'", "B", "B'"]
    lst = []
    for _ in range(count):
        move = random.choice(moves)
        lst.append(move)
    apply_moves(cube, lst)
    return lst

