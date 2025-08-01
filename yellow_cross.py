from moves import apply_moves

def is_yellow_cross_done(cube):
    return all([
        cube['D'][0][1] == 'Y',  # Up edge
        cube['D'][1][0] == 'Y',  # Left edge
        cube['D'][1][2] == 'Y',  # Right edge
        cube['D'][2][1] == 'Y',  # Down edge
    ])

def get_yellow_cross_pattern(cube):
    edges = [cube['D'][0][1], cube['D'][1][0], cube['D'][1][2], cube['D'][2][1]]
    yellow_edges = edges.count('Y')

    if yellow_edges == 0:
        return 'dot'
    elif yellow_edges == 2:
        if cube['D'][1][0] == 'Y' and cube['D'][1][2] == 'Y':
            return 'horizontal'
        elif cube['D'][0][1] == 'Y' and cube['D'][2][1] == 'Y':
            return 'vertical'
        else:
            return 'L'
    elif yellow_edges == 4:
        return 'cross'
    else:
        return 'L'  # fallback

def solve_yellow_cross(cube):
    algo = ["F", "L", "D", "L'", "D'", "F'"]
    attempts = 0
    moves = []

    while not is_yellow_cross_done(cube) and attempts < 5:
        pattern = get_yellow_cross_pattern(cube)

        if pattern == 'dot':
            moves.extend(algo)
            apply_moves(cube, algo)

        elif pattern == 'L':
            # Ensure Y on left and top to match 'L' in correct orientation
            for _ in range(4):
                if cube['D'][1][0] == 'Y' and cube['D'][0][1] == 'Y':
                    break
                moves.append('D')
                apply_moves(cube, ['D'])
            moves.extend(algo)
            apply_moves(cube, algo)

        elif pattern in ['horizontal', 'vertical']:
            # Rotate if it's vertical to align horizontally
            if pattern == 'vertical':
                moves.append('D')
                apply_moves(cube, ['D'])
            moves.extend(algo)
            apply_moves(cube, algo)

        attempts += 1

    return moves
