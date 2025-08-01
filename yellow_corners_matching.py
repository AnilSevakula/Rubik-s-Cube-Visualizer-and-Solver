from moves import apply_moves

def solve_yellow_corners_position(cube):
    moves = []

    def corners_in_place():
        corners = [
            (("D", (0, 0)), ("L", (2, 2)), ("F", (2, 0)), {"Y", "G", "O"}, "DLF"),
            (("D", (0, 2)), ("F", (2, 2)), ("R", (2, 0)), {"Y", "G", "R"}, "DFR"),
            (("D", (2, 2)), ("R", (2, 2)), ("B", (2, 0)), {"Y", "B", "R"}, "DRB"),
            (("D", (2, 0)), ("B", (2, 2)), ("L", (2, 0)), {"Y", "B", "O"}, "DBL"),
        ]
        matched = []
        for (f1, p1), (f2, p2), (f3, p3), expected, label in corners:
            actual = {cube[f1][p1], cube[f2][p2], cube[f3][p3]}
            if actual == expected:
                matched.append(label)
        return matched

    def rotate_cube_until(label):
        order = ["DLF", "DFR", "DRB", "DBL"]
        idx = order.index(label)
        num_rot = (4 - idx) % 4
        for _ in range(num_rot):
            apply_moves(cube, ["Y"])
            moves.append("Y")
        return num_rot

    def apply_corner_perm():
        alg = ["D", "L", "D'", "R'", "D", "L'", "D'", "R"]
        apply_moves(cube, alg)
        moves.extend(alg)

    for _ in range(6):
        matched = corners_in_place()

        if len(matched) == 4:
            return moves

        elif len(matched) >= 1:
            n = rotate_cube_until(matched[0])
            apply_corner_perm()
            for _ in range(n):
                apply_moves(cube, ["Y'"])
                moves.append("Y'")

        else:
            apply_corner_perm()

    print("⚠️ Loop exited — verify corner positions manually.")
    return moves
