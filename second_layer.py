from moves import apply_moves

def is_second_layer_solved(cube):
    for face in ["L", "F", "R", "B"]:
        if cube[face][1, 0] != cube[face][1, 1] or cube[face][1, 1] != cube[face][1, 2]:
            return False
    return True

def left_of(face):
    order = ['L', 'F', 'R', 'B']
    return order[(order.index(face) - 1) % 4]

def right_of(face):
    order = [ 'L', 'F', 'R', 'B']
    return order[(order.index(face) + 1) % 4]

def difference(face, actual_face):
    order = ['L', 'F', 'R', 'B']
    diff = order.index(actual_face) - order.index(face)
    if diff < 0:
        diff += 4
    return diff

def solve_second_layer(cube):
    moves = []
    seq = []

    def is_valid_edge(color1, color2):
        return color1 != 'Y' and color2 != 'Y'

    def insert_edge_to_left(cube, face, moves):
        if face == "L":
            seq = ["D", "B", "D", "B'", "D'", "L'", "D'", "L", "D"]
        elif face == "F":
            seq = ["D", "L", "D", "L'", "D'", "F'", "D'", "F", "D"]
        elif face == "R":
            seq = ["D", "F", "D", "F'", "D'", "R'", "D'", "R", "D"]
        elif face == "B":
            seq = ["D", "R", "D", "R'", "D'", "B'", "D'", "B", "D"]
        moves.extend(seq)
        apply_moves(cube, seq)

    def insert_edge_to_right(cube, face, moves):
        if face == "L":
            seq = ["D'", "F'", "D'", "F", "D", "L", "D", "L'", "D'"]
        elif face == "F":
            seq = ["D'", "R'", "D'", "R", "D", "F", "D", "F'", "D'"]
        elif face == "R":
            seq = ["D'", "B'", "D'", "B", "D", "R", "D", "R'", "D'"]
        elif face == "B":
            seq = ["D'", "L'", "D'", "L", "D", "B", "D", "B'", "D'"]
        moves.extend(seq)
        apply_moves(cube, seq)

    max_attempts = 8
    attempts = 0

    if is_second_layer_solved(cube):
        return moves

    while attempts < max_attempts:
        for face in [ 'L', 'F', 'R', 'B']:
            center_color = cube[face][1][1]
            edge_color = cube[face][2][1]
            top_color = cube['D'][0][1] if face == 'F' else \
                        cube['D'][1][2] if face == 'R' else \
                        cube['D'][2][1] if face == 'B' else \
                        cube['D'][1][0]
            if not is_valid_edge(edge_color, top_color):
                continue
            hashmap = {"B": "B", "R": "R", "O": "L", "G": "F"}
            actual_face = hashmap[edge_color]

            for _ in range(difference(face, actual_face)):
                moves.append("D")
                apply_moves(cube, ["D"])

            if top_color == cube[left_of(actual_face)][1][1]:
                insert_edge_to_left(cube, actual_face, moves)
            elif top_color == cube[right_of(actual_face)][1][1]:
                insert_edge_to_right(cube, actual_face, moves)
            else:
                moves.append("D'")
                apply_moves(cube, ["D'"])
        attempts += 1

    for _ in range(100):
        if is_second_layer_solved(cube):
            return moves
        for face in ["L", "F", "R", "B"]:
            for row, col in [(1, 0), (1, 2)]:
                if cube[face][row, col] != cube[face][1, 1]:
                    if col == 0:
                        insert_edge_to_left(cube, face, moves)
                    else:
                        insert_edge_to_right(cube, face, moves)
                    extra_moves = solve_second_layer(cube)
                    moves.extend(extra_moves)
                    return moves

    return moves
