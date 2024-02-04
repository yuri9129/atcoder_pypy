H, W, N = map(int, input().split())

grids = [[False] * W for _ in range(H)]

# 0: 上, 1: 右, 2: 下, 3: 左

def do_action(x, y, dir):
    if(grids[y][x]):
        # 黒だったら
        grids[y][x] = False
        dir = (dir - 1) % 4

    else:
        grids[y][x] = True
        dir = (dir + 1) % 4

    if dir == 0:
        y -= 1
    elif dir == 1:
        x += 1
    elif dir == 2:
        y += 1
    else:
        x -= 1
    return (x + W) % W, (y + H) % H, dir


def print_grids():
    for v in grids:
        a = ''
        for b in v:
            a += '#' if b else '.'
        print(a)

x, y, dir = 0, 0, 0
for _ in range(N):
    x, y, dir = do_action(x, y, dir)

print_grids()

