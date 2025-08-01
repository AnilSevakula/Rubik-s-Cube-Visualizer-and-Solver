from moves import possible_moves, apply_moves


def is_white_corners_done(cube):
    # Check each of the 4 D face corners
    # Corner positions and their adjacent faces
    corners = [
        (('U', (0, 0)), [('L', (0, 0)), ('B', (0, 2))]),  # Front-Left corner
        (('U', (0, 2)), [('R', (0, 2)), ('B', (0, 0))]),  # Front-Right corner
        (('U', (2, 0)), [('L', (0, 2)), ('F', (0, 0))]),  # Back-Right corner
        (('U', (2, 2)), [('F', (0, 2)), ('R', (0, 0))])  # Back-Left corner
    ]

    for (u_face, u_pos), adjacent in corners:
        if cube[u_face][u_pos] != 'W':
            return False
        # You can optionally also check if adjacent faces match their centers
        for face, pos in adjacent:
            if cube[face][pos] != cube[face][1][1]:  # Should match center color
                return False
    return True


def white_corner_solver(cube):
    def apply_moves_helper(moves):
        apply_moves(cube, moves)
        total_white_corner_moves.extend(moves)
    total_white_corner_moves = []
    for _ in range(200):
        if is_white_corners_done(cube):
            break
        move_made = False
        if cube["D"][0, 0] == "W" or cube["L"][2, 2] == "W" or cube["F"][2, 0] == "W":
            corner = {cube["D"][0, 0], cube["L"][2, 2], cube["F"][2, 0]}
            if corner == {"W", "G", "O"}:
                while cube["U"][2, 0] != "W" or cube["L"][0, 2] != "O" or cube["F"][0, 0] != "G":
                    apply_moves_helper(["L", "D", "L'", "D'"])
            elif corner == {"W", "B", "O"}:
                apply_moves_helper(["D'"])
                while cube["U"][0, 0] != "W" or cube["L"][0, 0] != "O" or cube["B"][0, 2] != "B":
                    apply_moves_helper(["B", "D", "B'", "D'"])
            elif corner == {"W", "B", "R"}:
                apply_moves_helper(["D'", "D'"])
                while cube["U"][0, 2] != "W" or cube["B"][0, 0] != "B" or cube["R"][0, 2] != "R":
                    apply_moves_helper(["R", "D", "R'", "D'"])
            elif corner == {"W", "R", "G"}:
                apply_moves_helper(["D"])
                while cube["U"][2, 2] != "W" or cube["F"][0, 2] != "G" or cube["R"][0, 0] != "R":
                    apply_moves_helper(["R'", "D'", "R", "D"])
            move_made = True
        if not move_made:
            if cube["D"][2, 0] == "W" or cube["L"][2, 0] == "W" or cube["B"][2, 2] == "W":
                corner = {cube["D"][2, 0], cube["L"][2, 0], cube["B"][2, 2]}
                if corner == {"W", "B", "O"}:
                    while cube["U"][0, 0] != "W" or cube["L"][0, 0] != "O" or cube["B"][0, 2] != "B":
                        apply_moves_helper(["B", "D", "B'", "D'"])
                elif corner == {"W", "B", "R"}:
                    apply_moves_helper(["D'"])
                    while cube["U"][0, 2] != "W" or cube["B"][0, 0] != "B" or cube["R"][0, 2] != "R":
                        apply_moves_helper(["R", "D", "R'", "D'"])
                elif corner == {"W", "G", "R"}:
                    apply_moves_helper(["D", "D"])
                    while cube["U"][2, 2] != "W" or cube["R"][0, 0] != "R" or cube["F"][0, 2] != "G":
                        apply_moves_helper(["R'", "D'", "R", "D"])
                elif corner == {"W", "O", "G"}:
                    apply_moves_helper(["D"])
                    while cube["U"][2, 0] != "W" or cube["F"][0, 0] != "G" or cube["L"][0, 2] != "O":
                        apply_moves_helper(["L", "D", "L'", "D'"])

                move_made = True
        if not move_made:
            if cube["D"][0, 2] == "W" or cube["R"][2, 0] == "W" or cube["F"][2, 2] == "W":
                corner = {cube["D"][0, 2], cube["R"][2, 0], cube["F"][2, 2]}
                if corner == {"W", "G", "R"}:
                    while cube["U"][2,2] != "W" or cube["R"][0, 0] != "R" or cube["F"][0, 2] != "G":
                        apply_moves_helper(["R'", "D'", "R", "D"])
                elif corner == {"W", "B", "R"}:
                    apply_moves_helper(["D"])
                    while cube["U"][0, 2] != "W" or cube["B"][0, 0] != "B" or cube["R"][0, 2] != "R":
                        apply_moves_helper(["R", "D", "R'", "D'"])
                elif corner == {"W", "B", "O"}:
                    apply_moves_helper(["D", "D"])
                    while cube["U"][0, 0] != "W" or cube["L"][0, 0] != "O" or cube["B"][0, 2] != "B":
                        apply_moves_helper(["B", "D", "B'", "D'"])
                elif corner == {"W", "O", "G"}:
                    apply_moves_helper(["D'"])
                    while cube["U"][2, 0] != "W" or cube["F"][0, 0] != "G" or cube["L"][0, 2] != "O":
                        apply_moves_helper(["L", "D", "L'", "D'"])
                move_made = True
        if not move_made:
            if cube["D"][2, 2] == "W" or cube["R"][2, 2] == "W" or cube["B"][2, 0] == "W":
                corner = {cube["D"][2, 2], cube["R"][2, 2], cube["B"][2, 0]}
                if corner == {"W", "B", "R"}:
                    while cube["U"][0, 2] != "W" or cube["R"][0, 2] != "R" or cube["B"][0, 0] != "B":
                        apply_moves_helper(["R", "D", "R'", "D'"])
                elif corner == {"W", "G", "R"}:
                    apply_moves_helper(["D'"])
                    while cube["U"][2, 2] != "W" or cube["F"][0, 2] != "G" or cube["R"][0, 0] != "R":
                        apply_moves_helper(["R'", "D'", "R", "D"])
                elif corner == {"W", "G", "O"}:
                    apply_moves_helper(["D", "D"])
                    while cube["U"][2, 0] != "W" or cube["L"][0, 2] != "O" or cube["F"][0, 0] != "G":
                        apply_moves_helper(["L", "D", "L'", "D'"])
                elif corner == {"W", "B", "O"}:
                    apply_moves_helper(["D"])
                    while cube["U"][0, 0] != "W" or cube["L"][0, 0] != "O" or cube["B"][0, 2] != "B":
                        apply_moves_helper(["B", "D", "B'", "D'"])
                move_made = True

        # case 2: in the white face
        moves = []
        if not move_made:
            if cube["U"][0, 0] == "W" or cube["L"][0, 0] == "W" or cube["B"][0, 2] == "W":
                if cube["U"][0, 0] != "W" or cube["L"][0, 0] != "O" or cube["B"][0, 2] != "B":
                    moves = ["B", "D", "B'", "D'"]
                    move_made = True
        if not move_made:
            if cube["U"][0, 2] == "W" or cube["R"][0, 2] == "W" or cube["B"][0, 0] == "W":
                if cube["U"][0, 2] != "W" or cube["R"][0, 2] != "R" or cube["B"][0, 0] != "B":
                    moves = ["R", "D", "R'", "D'"]
                    move_made = True
        if not move_made:
            if cube["U"][2, 0] == "W" or cube["L"][0, 2] == "W" or cube["F"][0, 0] == "W":
                if cube["U"][2, 0] != "W" or cube["L"][0, 2] != "O" or cube["F"][0, 0] != "G":
                    moves = ["L", "D", "L'", "D'"]
                    move_made = True
        if not move_made:
            if cube["U"][2, 2] == "W" or cube["R"][0, 0] == "W" or cube["F"][0, 2] == "W":
                if cube["U"][2, 2] != "W" or cube["F"][0, 2] != "G" or cube["R"][0, 0] != "R":
                    moves = ["R'", "D'", "R", "D"]
                    move_made = True
        if moves:
            apply_moves(cube, moves)
            total_white_corner_moves.extend(moves)
    return total_white_corner_moves
