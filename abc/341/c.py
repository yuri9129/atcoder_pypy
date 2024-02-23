H, W, N = map(int, input().split())
moves = list(input())
maps = [list(input()) for _ in range(H)]

routes = [(0,0)]
for move in moves:
    x, y = routes[-1]
    if move == 'U':
        x -= 1
    elif move == 'D':
        x += 1
    elif move == 'L':
        y -= 1
    else:
        y += 1
    routes.append((x, y))

routes = set(routes)
# for a, b in routes:
#     print(a, b)

def check_routes(init_x, init_y):

    for route in routes:
        x = init_x + route[0]
        y = init_y + route[1]
        if x < 0 or x >= H or y < 0 or y >= W or maps[x][y] == '#':
            return False
    # print(init_x, init_y)
    return True

ret = 0
for x in range(H):
    for y in range(W):
        if maps[x][y] == '#':
            continue
        if check_routes(x, y):
            ret += 1

print(ret)


