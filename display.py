def print_cube(cube):
    print("\t\tUP")
    for row in cube['U']:
        print("\t\t", end='')
        for col in row:
            print(col, end=' ')
        print()
    print("Left \tFront\tRight\tBack")
    for row in range(3):
        for col in range(3):
            print(cube['L'][row][col], end=' ')
        print("\t", end='')
        for col in range(3):
            print(cube['F'][row][col], end=' ')
        print("\t", end='')
        for col in range(3):
            print(cube['R'][row][col], end=' ')
        print("\t", end='')
        for col in range(3):
            print(cube['B'][row][col], end=' ')
        print()
    print("\t\tDown")
    for row in cube['D']:
        print("\t\t", end='')
        for col in row:
            print(col, end=' ')
        print()