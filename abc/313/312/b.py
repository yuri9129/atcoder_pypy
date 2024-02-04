n, m = map(int, input().split())
cells = [list(input()) for _ in range(n)]

def is_takcode(i, j):
    global cells
    blacks = [
        (0, 0),
        (0, 1),
        (0, 2),
        (1, 0),
        (1, 1),
        (1, 2),
        (2, 0),
        (2, 1),
        (2, 2),
        (6, 6),
        (6, 7),
        (6, 8),
        (7, 6),
        (7, 7),
        (7, 8),
        (8, 6),
        (8, 7),
        (8, 8),
    ]
    whites = [
        (0, 3),
        (1, 3),
        (2, 3),
        (3, 0),
        (3, 1),
        (3, 2),
        (3, 3),
        (5, 5),
        (5, 6),
        (5, 7),
        (5, 8),
        (6, 5),
        (7, 5),
        (8, 5),
    ]

    for x, y in blacks:
        if(cells[i + x][j + y] != '#'):
            # print(f"({i + x},{j + y})は黒ではありません")
            return False

    for x, y in whites:
        if(cells[i + x][j + y] != '.'):
            # print(f"({i + x},{j + y})は白ではありません")
            return False

    return True

for x in range(n - 8):
    for y in range(m - 8):
        if (is_takcode(x, y)):
            print(f"{x + 1} {y + 1}")

