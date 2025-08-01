import numpy as np

def possible_moves(c, move):
    if move == 'U':  # Up clockwise
        c['U'] = np.rot90(c['U'], k=-1)
        temp = c['F'][0].copy()
        c['F'][0] = c['R'][0]
        c['R'][0] = c['B'][0]
        c['B'][0] = c['L'][0]
        c['L'][0] = temp
    elif move == "U'":  # Up counter-clockwise
        c['U'] = np.rot90(c['U'], k=1)
        temp = c['F'][0].copy()
        c['F'][0] = c['L'][0]
        c['L'][0] = c['B'][0]
        c['B'][0] = c['R'][0]
        c['R'][0] = temp
    elif move == 'D':  # Down clockwise
        c['D'] = np.rot90(c['D'], k=-1)
        temp = c['F'][2].copy()
        c['F'][2] = c['L'][2]
        c['L'][2] = c['B'][2]
        c['B'][2] = c['R'][2]
        c['R'][2] = temp
    elif move == "D'":  # Down counter-clockwise
        c['D'] = np.rot90(c['D'], k=1)
        temp = c['F'][2].copy()
        c['F'][2] = c['R'][2]
        c['R'][2] = c['B'][2]
        c['B'][2] = c['L'][2]
        c['L'][2] = temp
    elif move == 'L':  # Left clockwise
        c['L'] = np.rot90(c['L'], k=-1)
        temp = c['F'][:, 0].copy()
        c['F'][:, 0] = c['U'][:, 0]
        c['U'][:, 0] = c['B'][::-1, 2]
        c['B'][:, 2] = c['D'][::-1, 0]
        c['D'][:, 0] = temp
    elif move == "L'":  # Left counter-clockwise
        c['L'] = np.rot90(c['L'], k=1)
        temp = c['F'][:, 0].copy()
        c['F'][:, 0] = c['D'][:, 0]
        c['D'][:, 0] = c['B'][:, 2][::-1]
        c['B'][:, 2] = c['U'][:, 0][::-1]
        c['U'][:, 0] = temp
    elif move == 'R':  # Right clockwise
        c['R'] = np.rot90(c['R'], k=-1)
        temp = c['F'][:, 2].copy()
        c['F'][:, 2] = c['D'][:, 2]
        c['D'][:, 2] = c['B'][:, 0][::-1]
        c['B'][:, 0] = c['U'][:, 2][::-1]
        c['U'][:, 2] = temp
    elif move == "R'":  # Right counter-clockwise
        c['R'] = np.rot90(c['R'], k=1)
        temp = c['F'][:, 2].copy()
        c['F'][:, 2] = c['U'][:, 2]
        c['U'][:, 2] = c['B'][:, 0][::-1]
        c['B'][:, 0] = c['D'][:, 2][::-1]
        c['D'][:, 2] = temp
    elif move == 'F':  # Front clockwise
        c['F'] = np.rot90(c['F'], k=-1)
        temp = c['U'][2].copy()
        c['U'][2] = c['L'][:, 2][::-1]
        c['L'][:, 2] = c['D'][0]
        c['D'][0] = c['R'][:, 0][::-1]
        c['R'][:, 0] = temp
    elif move == "F'":  # Front counter-clockwise
        c['F'] = np.rot90(c['F'], k=1)
        temp = c['U'][2].copy()
        c['U'][2] = c['R'][:, 0]
        c['R'][:, 0] = c['D'][0][::-1]
        c['D'][0] = c['L'][:, 2]
        c['L'][:, 2] = temp[::-1]
    elif move == 'B':  # Back clockwise
        c['B'] = np.rot90(c['B'], k=-1)
        temp = c['U'][0].copy()
        c['U'][0] = c['R'][:, 2]
        c['R'][:, 2] = c['D'][2][::-1]
        c['D'][2] = c['L'][:, 0]
        c['L'][:, 0] = temp[::-1]
    elif move == "B'":  # Back counter-clockwise
        c['B'] = np.rot90(c['B'], k=1)
        temp = c['U'][0].copy()
        c['U'][0] = c['L'][:, 0][::-1]
        c['L'][:, 0] = c['D'][2]
        c['D'][2] = c['R'][:, 2][::-1]
        c['R'][:, 2] = temp
    elif move == 'Y':  # Whole cube rotation clockwise around Y-axis
        # Rotate U and D faces
        c['U'] = np.rot90(c['U'], k=1)  # CW
        c['D'] = np.rot90(c['D'], k=-1)   # CCW

        # Cycle side faces: F → R → B → L → F
        temp = c['F'].copy()
        c['F'] = c['L']
        c['L'] = c['B']
        c['B'] = c['R']
        c['R'] = temp

    elif move == "Y'":  # Whole cube rotation counter-clockwise around Y-axis
        c['U'] = np.rot90(c['U'], k=-1)   # CCW
        c['D'] = np.rot90(c['D'], k=1)  # CW

        # Cycle side faces: F → L → B → R → F
        temp = c['F'].copy()
        c['F'] = c['R']
        c['R'] = c['B']
        c['B'] = c['L']
        c['L'] = temp

    else:
        raise ValueError(f"Invalid move: {move}")


def apply_moves(cube, moves):
    for move in moves:
        possible_moves(cube, move)