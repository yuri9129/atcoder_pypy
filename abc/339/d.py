from collections import deque

N = int(input())
grids = [list(input()) for _ in range(N)]

# queue = deque()
queue = []
all_cnt = 0

def print_grids():
    for v in grids:
        print("".join(v))

# 訪問済みのマス
# [x1][y1][x2][y2]
checked_grids = [list(list([False] * N for _ in range(N)) for _ in range(N)) for _ in range(N)]

# 各マスまでの操作回数
cnt_grids = [list(list([10**10] * N for _ in range(N)) for _ in range(N)) for _ in range(N)]

# プレイヤーの座標を取得
x1, y1, x2, y2 = None, None, None, None
for x, a in enumerate(grids):
    for y, b in enumerate(a):
        if b == 'P':
            if x1 is None:
                x1, y1 = x, y
            else:
                x2, y2 = x, y


def move(x, y, dir):
    after_x, after_y = None, None
    if dir == 'U':
        after_x, after_y = x - 1, y
    elif dir == 'D':
        after_x, after_y = x + 1, y
    elif dir == 'L':
        after_x, after_y = x, y - 1
    elif dir == 'R':
        after_x, after_y = x, y + 1


    if(after_x < 0 or after_x >= N or after_y < 0 or after_y >= N):
        return x, y
    elif(grids[after_x][after_y] == '#'):
        return x, y

    return after_x, after_y


def dfs(p1, p2, cnt):
    global all_cnt
    all_cnt += 1
    x1, y1 = p1
    x2, y2 = p2

    if(cnt_grids[x1][y1][x2][y2] <= cnt):
        # すでに最小手数で到達済みなのでこれ以上探索は不要
        return

    cnt_grids[x1][y1][x2][y2] = cnt

    cnt += 1
    for d in ['U', 'D', 'L', 'R']:
        tmp_p1, tmp_p2 = move(x1, y1, d), move(x2, y2, d)
        tmp_x1, tmp_y1 = tmp_p1
        tmp_x2, tmp_y2 = tmp_p2
        if(cnt_grids[tmp_x1][tmp_y1][tmp_x2][tmp_y2] <= cnt):
            continue
        elif(checked_grids[tmp_x1][tmp_y1][tmp_x2][tmp_y2]):
            continue
        else:
            checked_grids[tmp_x1][tmp_y1][tmp_x2][tmp_y2] = True
            queue.append([tmp_p1, tmp_p2, cnt])


queue.append([(x1, y1), (x2, y2), 0])
checked_grids[x1][y1][x2][y2] = True

while len(queue) > 0:
    # q = queue.popleft()
    q = queue.pop()
    dfs(q[0], q[1], q[2])


ret = 10**10
for x in range(N):
    for y in range(N):
        ret = min(ret, cnt_grids[x][y][x][y])

if ret == 10**10:
    print(-1)
else:
    print(ret)

# print(all_cnt)