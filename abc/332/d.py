H, W = map(int, input().split())

def p():
    print("=== A ===")
    for v in grid_a:
        print(*[str(a).rjust(2, ' ') for a in v])

    print("=== B ===")
    for v in grid_b:
        print(*[str(a).rjust(2, ' ') for a in v])


def change_row(grid, row):
    grid[row], grid[row+1] = (grid[row+1], grid[row])

def change_col(grid, col):
    for i in range(H):
        grid[i][col], grid[i][col + 1] = (grid[i][col + 1], grid[i][col])

def count_val(grid):
    ret = {}
    for row in grid:
        for v in row:
            ret[v] = ret.get(v, 0) + 1
    return ret

def check():
    cnt_a = count_val(grid_a)
    cnt_b = count_val(grid_b)

    for k, v in cnt_a.items():
        if v != cnt_b.get(k, 0):
            return False
    return True


def is_same():
    for i in range(H):
        for j in range(W):
            if grid_a[i][j] != grid_b[i][j]:
                return False

    return True

grid_a = [list(map(int, input().split())) for _ in range(H)]
grid_b = [list(map(int, input().split())) for _ in range(H)]

p()
exit()

checked_a = [False for _ in range(H)]
checked_b = [False for _ in range(H)]
for i in range(H):
    row_a = grid_a[i]
    for j in range(H):
        if checked_b[j]:
            continue
        row_b = grid_b[j]
        if(sorted(row_a) == sorted(row_b)):
            checked_b[j] = True
            print(row_a, row_b)


if len([v for v in checked_b if v == False]):
    print("NG")
else:
    print("OK")


checked_a = [False for _ in range(W)]
checked_b = [False for _ in range(W)]
for i in range(W):
    col_a = [row[i] for row in grid_a]
    for j in range(W):
        if checked_b[j]:
            continue
        col_b = [row[j] for row in grid_b]
        if(sorted(col_a) == sorted(col_b)):
            checked_a[i] = True
            checked_b[j] = True

if len([v for v in checked_b if v == False]):
    print("NG")
else:
    print("OK")



