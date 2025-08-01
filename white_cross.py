from moves import apply_moves

def is_white_cross_done(cube):
    return (
        cube['U'][0, 1] == 'W' and
        cube['U'][1, 0] == 'W' and
        cube['U'][1, 2] == 'W' and
        cube['U'][2, 1] == 'W' and
        cube['L'][0, 1] == cube['L'][1, 1] and
        cube['F'][0, 1] == cube['F'][1, 1] and
        cube['R'][0, 1] == cube['R'][1, 1] and
        cube['B'][0, 1] == cube['B'][1, 1]
    )

def white_cross_solver(cube):
    """This function solves for white cross"""
    max_iterations = 200
    total_white_cross_moves = []

    def down_edge_cases():
        """Check for white edge on Down face and return corresponding moves."""
        for row, col in [(0, 1), (1, 0), (1, 2), (2, 1)]:
            if cube['D'][row, col] == 'W':
                if row == 0 and col == 1:
                    if cube['F'][2, 1] == cube['F'][1, 1]:
                        return ["F", "F"]
                    elif cube['F'][2, 1] == 'R':
                        return ["D", "R", "R"]
                    elif cube['F'][2, 1] == 'O':
                        return ["D'", "L", "L"]
                    elif cube['F'][2, 1] == 'B':
                        return ["D", "D", "B", "B"]
                elif row == 1 and col == 0:
                    if cube['L'][2, 1] == cube['L'][1, 1]:
                        return ["L", "L"]
                    elif cube['L'][2, 1] == 'G':
                        return ["D", "F", "F"]
                    elif cube['L'][2, 1] == 'B':
                        return ["D'", "B", "B"]
                    elif cube['L'][2, 1] == 'R':
                        return ["D", "D", "R", "R"]
                elif row == 1 and col == 2:
                    if cube['R'][2, 1] == cube['R'][1, 1]:
                        return ["R", "R"]
                    elif cube['R'][2, 1] == 'B':
                        return ["D", "B", "B"]
                    elif cube['R'][2, 1] == 'G':
                        return ["D'", "F", "F"]
                    elif cube['R'][2, 1] == 'O':
                        return ["D", "D", "L", "L"]
                elif row == 2 and col == 1:
                    if cube['B'][2, 1] == cube['B'][1, 1]:
                        return ["B", "B"]
                    elif cube['B'][2, 1] == 'O':
                        return ["D", "L", "L"]
                    elif cube['B'][2, 1] == 'R':
                        return ["D'", "R", "R"]
                    elif cube['B'][2, 1] == 'G':
                        return ["D", "D", "F", "F"]
        return None

    def bottom_side_cases():
        """Check for white edge on the bottommost row of side faces."""
        for face in ['L', 'F', 'R', 'B']:
            c = cube[face][2, 1]
            if c == 'W':
                if face == 'L':
                    if cube['D'][1, 0] == 'R':
                        return ["D", "D", "R'", "U'", "B", "U"]
                    elif cube['D'][1, 0] == 'G':
                        return ["D", "F", "U'", "R", "U"]
                    elif cube['D'][1, 0] == 'B':
                        return ["D'", "B'", "U'", "L", "U"]
                    else:
                        return ["L", "L"]
                elif face == 'F':
                    if cube['D'][0, 1] == 'B':
                        return ["D", "D", "B'", "U'", "L", "U"]
                    elif cube['D'][0, 1] == 'R':
                        return ["D", "R'", "U'", "B", "U"]
                    elif cube['D'][0, 1] == 'O':
                        return ["D'", "L'", "U'", "F", "U"]
                    else:
                        return ["F", "F"]
                elif face == 'R':
                    if cube['D'][1, 2] == 'O':
                        return ["D", "D", "L'", "U'", "F", "U"]
                    elif cube['D'][1, 2] == 'B':
                        return ["D", "B'", "U'", "L", "U"]
                    elif cube['D'][1, 2] == 'G':
                        return ["D'", "F", "U'", "R", "U"]
                    else:
                        return ["R", "R"]
                elif face == 'B':
                    if cube['D'][2, 1] == 'G':
                        return ["D", "D", "F", "U'", "R", "U"]
                    elif cube['D'][2, 1] == 'O':
                        return ["D", "L'", "U'", "F", "U"]
                    elif cube['D'][2, 1] == 'R':
                        return ["D'", "R'", "U'", "B", "U"]
                    else:
                        return ["B", "B"]
        return None

    def side_edge_cases():
        """Check for white edge in side-middle positions."""
        for face in ['L', 'F', 'R', 'B']:
            for row, col in [(1, 0), (1, 2)]:
                if cube[face][row, col] == 'W':
                    if row == 1 and col == 0:
                        if face == 'F':
                            return ["L", "D", "L'"]
                        elif face == 'L':
                            return ["B", "D", "B'"]
                        elif face == 'R':
                            return ["F", "D", "F'"]
                        elif face == 'B':
                            return ["R", "D", "R'"]
                    elif row == 1 and col == 2:
                        if face == 'F':
                            return ["R'", "D'", "R"]
                        elif face == 'L':
                            return ["F'", "D'", "F"]
                        elif face == 'R':
                            return ["B'", "D'", "B"]
                        elif face == 'B':
                            return ["L'", "D'", "L"]
        return None

    def u_face_cases():
        """Check for white edge on U face middle-edge positions."""
        for face in ['L', 'F', 'R', 'B']:
            if cube[face][0, 1] == 'W':
                if face == 'L':
                    return ["B'", "F", "L'", "B", "F'"]
                elif face == 'F':
                    return ["R", "L'", "F'", "R'", "L"]
                elif face == 'R':
                    return ["B", "F'", "R'", "B'", "F"]
                elif face == 'B':
                    return ["R'", "L", "B'", "R'", "L"]
        return None

    def misaligned_u_cases():
        """Check for misaligned white edges on U face."""
        checks = [
            ((0, 1), "B", cube["B"][0, 1] != cube["B"][1, 1], ["R'", "L", "B'", "R'", "L"]),
            ((1, 0), "L", cube["L"][0, 1] != cube["L"][1, 1], ["B'", "F", "L'", "B", "F'"]),
            ((1, 2), "R", cube["R"][0, 1] != cube["R"][1, 1], ["B", "F'", "R'", "B'", "F"]),
            ((2, 1), "F", cube["F"][0, 1] != cube["F"][1, 1], ["R", "L'", "F'", "R'", "L"]),
        ]
        for (row, col), face, condition, movelist in checks:
            if cube["U"][row, col] == "W" and condition:
                return movelist
        return None

    for _ in range(max_iterations):
        if is_white_cross_done(cube):
            break
        moves = (
            down_edge_cases() or
            bottom_side_cases() or
            side_edge_cases() or
            u_face_cases() or
            misaligned_u_cases()
        )
        if moves is None:
            raise ValueError("Stuck solving white cross. Check cube state.")
        apply_moves(cube, moves)
        total_white_cross_moves.extend(moves)

    return total_white_cross_moves
