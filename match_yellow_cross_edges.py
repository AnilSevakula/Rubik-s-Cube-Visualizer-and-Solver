from moves import apply_moves

def is_yellow_cross_edges_matched(cube):
    for face in ["L", "F", "R", "B"]:
        if cube[face][2, 1] != cube[face][1, 1]:
            return False
    return True

def solve_yellow_edge_matching(cube):
    moves = []

    def get_matching_edges():
        faces = ['F', 'R', 'B', 'L']
        return [face for face in faces if cube[face][2][1] == cube[face][1][1]]

    def rotate_d_until_match_at_back(face):
        faces = ['F', 'R', 'B', 'L']
        idx = faces.index(face)
        count = 0
        while faces[(idx % 4)] != 'R':
            apply_moves(cube, ['D'])
            moves.append('D')
            idx += 1
            count += 1
        return count

    def apply_yellow_edge_algorithm():
        alg = ["L", "D", "L'", "D", "L", "D'", "D'", "L'"]
        apply_moves(cube, alg)
        moves.extend(alg)

    attempts = 0
    while attempts < 6:
        matched = get_matching_edges()
        if len(matched) == 4:
            return moves
        if len(matched) == 1 or len(matched) == 2:
            rotate_d_until_match_at_back(matched[0])
            apply_yellow_edge_algorithm()
        else:
            apply_moves(cube, ["D"])
            moves.append("D")
        attempts += 1
    if not is_yellow_cross_edges_matched(cube):
        moves.extend(solve_yellow_edge_matching2(cube))
    return moves

def solve_yellow_edge_matching2(cube):
    moves = []

    def get_matching_edges():
        faces = ['F', 'R', 'B', 'L']
        return [face for face in faces if cube[face][2][1] == cube[face][1][1]]

    def rotate_d_until_match_at_back(face):
        faces = ['F', 'R', 'B', 'L']
        idx = faces.index(face)
        count = 0
        while faces[(idx % 4)] != 'B':
            apply_moves(cube, ['D'])
            moves.append('D')
            idx += 1
            count += 1
        return count

    def apply_yellow_edge_algorithm():
        alg = ["L", "D", "L'", "D", "L", "D'", "D'", "L'"]
        apply_moves(cube, alg)
        moves.extend(alg)

    attempts = 0
    while attempts < 6:
        matched = get_matching_edges()
        if len(matched) == 4:
            return moves
        if len(matched) == 1 or len(matched) == 2:
            rotate_d_until_match_at_back(matched[0])
            apply_yellow_edge_algorithm()
        else:
            apply_moves(cube, ["D"])
            moves.append("D")
        attempts += 1
    return moves
