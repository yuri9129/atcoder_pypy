
N = int(input())

lst = [list(input()) for _ in range(N)]
ret = [[v for v in row] for row in lst]
for i, row in enumerate(lst):
    for j, v in enumerate(row):
        if i == 0:
            if j == N-1:
                ret[i + 1][j] = v
                continue
            else:
                ret[i][j + 1] = v
                continue
        if j == N-1:
            if i == N-1:
                ret[i][j - 1] = v
                continue
            else:
                ret[i + 1][j] = v
                continue
        if i == N-1:
            if j == 0:
                ret[i - 1][j] = v
                continue
            else:
                ret[i][j - 1] = v
                continue
        if j == 0:
            if i == 0:
                ret[i][j + 1] = v
                continue
            else:
                ret[i - 1][j] = v
                continue

        ret[i][j] = v

for row in ret:
    print("".join(row))
