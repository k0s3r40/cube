U = [[0, 0, 0]] * 3
D = [[1, 1, 1]] * 3

F = [[2, 2, 2]] * 3
B = [[3, 3, 3]] * 3

L = [[4, 4, 4]] * 3
R = [[5, 5, 5]] * 3

cube = [U, D, F, B, L, R]


def rotate(cube, axis='y', direction='-', r=0, times=1):
    for t in range(times):
        states = []
        if axis == 'x':
            for index, row in enumerate(cube):
                if direction == '-':
                    states.append(cube[index + 1 if index + 1 <= 5 else 0][r])
                if direction == '+':
                    states.append(cube[index - 1 if index - 1 >= 0 else 5][r])

        if axis == 'y':
            for index, col in enumerate(cube):
                if direction == '-':
                    states.append(cube[index + 1 if index + 1 <= 5 else 0][r][r])
                if direction == '+':
                    states.append(cube[index - 1 if index - 1 >= 0 else 5][r][r])
            for index, row in enumerate(cube):
                cube[index][r][r] = states[index]

    cube =  cube


cube = rotate(cube, axis='y', direction='+')
cube = rotate(cube, axis='y', direction='+')
cube = rotate(cube, axis='y', direction='+')

cube = rotate(cube, axis='x', direction='+')
cube = rotate(cube, axis='x', direction='+')
cube = rotate(cube, axis='x', direction='+')

cube = rotate(cube, axis='x', direction='-')
cube = rotate(cube, axis='x', direction='-')
cube = rotate(cube, axis='x', direction='-')

cube = rotate(cube, axis='y', direction='-')
cube = rotate(cube, axis='y', direction='-')
cube = rotate(cube, axis='y', direction='-')

for i in cube:
    print(i)
