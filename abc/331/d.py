N, Q = map(int, input().split())

maps = [input() for _ in range(N)]

def get_val(x, y): return maps[x][y]

def get_cum_sum():
    cum_sum = [[0] * (N + 1) for _ in range(N + 1)]
    for i in range(N):
        for j in range(N):
            cum_sum[i + 1][j + 1] += (1 if get_val(i, j) == 'B' else 0)
    for i in range(N + 1):
        for j in range(1, N + 1):
            cum_sum[i][j] += cum_sum[i][j-1]
    for j in range(N + 1):
        for i in range(1, N + 1):
            cum_sum[i][j] += cum_sum[i-1][j]
    return cum_sum

def get_blacks(X, Y):
    global cum_sum
    x = X + 1
    y = Y + 1

    ret = 0
    # print(f"x // N = {x // N}")
    # print(f"y // N = {y // N}")
    # print(f"X % N = {X % N}")
    # print(f"Y % N = {Y % N}")
    ret += (x // N) * (y // N) * cum_sum[N][N]

    ret += cum_sum[x % N][y % N]

    ret += (x // N) * cum_sum[N][y % N]
    ret += (y // N) * cum_sum[x % N][N]
    return ret

cum_sum = get_cum_sum()

for _ in range(Q):
    A, B, C, D = map(int, input().split())
    ret = get_blacks(C, D) - get_blacks(A - 1, D) - get_blacks(C, B - 1) + get_blacks(A - 1, B - 1)
    print(ret)




