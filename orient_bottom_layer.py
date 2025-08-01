from moves import apply_moves, possible_moves

def is_corner_oriented(corner):
    # We expect yellow ('Y') to be on the D face
    return corner[2] == 'Y'

def get_d_corners(cube):
    return {
        'DRF': [cube['D'][0][2], cube['R'][2][0], cube['F'][2][2]],
        'DLF': [cube['D'][0][0], cube['L'][2][2], cube['F'][2][0]],
        'DLB': [cube['D'][2][0], cube['L'][2][0], cube['B'][2][0]],
        'DRB': [cube['D'][2][2], cube['R'][2][2], cube['B'][2][2]],
    }

def all_bottom_corners_oriented(cube):
    for corner in get_d_corners(cube).values():
        if corner[0] != 'Y':  # D facelet is not yellow
            return False
    return True

def orient_bottom_yellow_corners(cube):
    moves = []
    attempts = 0

    # Step 1: Repeatedly orient corners with (R U R' U') at front-right (DRF)
    while not all_bottom_corners_oriented(cube) and attempts < 20:
        while cube['D'][0][2] != 'Y':
            seq = ["R", "U", "R'", "U'"]
            apply_moves(cube, seq)
            moves.extend(seq)
        apply_moves(cube, ["D"])
        moves.append("D")
        attempts += 1

    # Step 2: Optionally rotate D face until front left (F[2,0]) is green
    while cube["F"][2, 0] != "G":
        possible_moves(cube, "D")
        moves.append("D")

    return moves
