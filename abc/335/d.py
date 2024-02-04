N = int(input())

grid = [[-1] * N for _ in range(N)]

grid[(N - 1) // 2][(N - 1) // 2] = 0


pos = [0, 0]
direction = "R"
grid[pos[0]][pos[1]] = 1

for i in range(2, N*N):
    if direction == 'R':
        pos = [pos[0] + 1, pos[1]]
        grid[pos[0]][pos[1]] = i
        if pos[0] + 1 >= N or grid[pos[0] + 1][pos[1]] != -1:
            direction = 'D'
    elif direction == 'D':
        pos = [pos[0], pos[1] + 1]
        grid[pos[0]][pos[1]] = i
        if pos[1] + 1 >= N or grid[pos[0]][pos[1] + 1] != -1:
            direction = 'L'

    elif direction == 'L':
        pos = [pos[0] - 1, pos[1]]
        grid[pos[0]][pos[1]] = i
        if pos[0] - 1 < 0 or grid[pos[0] - 1][pos[1]] != -1:
            direction = 'U'
    elif direction == 'U':
        pos = [pos[0], pos[1] - 1]
        grid[pos[0]][pos[1]] = i
        if pos[1] - 1 < 0 or grid[pos[0]][pos[1] - 1] != -1:
            direction = 'R'


grid[(N - 1) // 2][(N - 1) // 2] = 'T'
for v in grid:
    print(" ".join(map(str, v)))

