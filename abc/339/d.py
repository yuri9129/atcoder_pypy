from collections import deque
# import time
# start_time = time.time()

def move(x, y, dir):
    tmp_x = x + dir[0]
    tmp_y = y + dir[1]
    if tmp_x < 0 or tmp_x >= N or tmp_y < 0 or tmp_y >= N or grids[tmp_x][tmp_y] == '#':
        return x, y
    return tmp_x, tmp_y

N = int(input())
grids = [list(input()) for _ in range(N)]

# 各パターンまでの最短手数
# dist = [list(list([10**18] * N for _ in range(N)) for _ in range(N)) for _ in range(N)]
dist = [[10**18] * (N**2) for _ in range(N**2)]
# print("--- %s seconds ---" % (time.time() - start_time))
queue = deque()

dirs = [[1,0], [0,1], [-1,0], [0,-1]]

players = []
for i in range(N):
    for j in range(N):
        if grids[i][j] == 'P':
            players.append((i, j))


p1 = players[0]
p2 = players[1]

queue.append([p1[0], p1[1], p2[0], p2[1]])
dist[p1[0] * N + p1[1]][p2[0] * N + p2[1]] = 0
while queue:
    x1, y1, x2, y2 = queue.popleft()
    for d in dirs:
        tx1, ty1 = move(x1, y1, d)
        tx2, ty2 = move(x2, y2, d)

        if (tx1 == x1 and ty1 == y1 and tx2 == x2 and ty2 == y2):
            continue

        if(tx1 == tx2 and ty1 == ty2):
            print(dist[x1 * N + y1][x2 * N + y2] + 1)
            print("--- %s seconds ---" % (time.time() - start_time))
            exit()

        if (dist[tx1 * N + ty1][tx2 * N + ty2] > dist[x1 * N + y1][x2 * N + y2] + 1):
            dist[tx1 * N + ty1][tx2 * N + ty2] = dist[x1 * N + y1][x2 * N + y2] + 1
            queue.append([tx1, ty1, tx2, ty2])

ret = 10**18
for i in range(N):
    k1 = i * N
    for j in range(N):
        k2 = k1 + j
        if dist[k2][k2] < ret:
            ret = dist[k2][k2]

if ret == 10**18:
    print(-1)
else:
    print(ret)


# print("--- %s seconds ---" % (time.time() - start_time))