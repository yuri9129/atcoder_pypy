def cnt_change(a,b):
    is_checked = [False] * len(a)
    a2 = []
    for a_k, a_v in enumerate(a):
        for b_k, b_v in enumerate(b):
            if(is_checked[b_k]):
                continue
            if(a_v == b_v):
                a2.append(b_k)
                is_checked[b_k] = True
                break

    cnt = 0
    for k in range(len(a2)):
        for l in range(k+1, len(a2)):
            if a2[k] > a2[l]:
                cnt += 1
    return cnt

def check():
    cnt_row = 0
    checked_b = [False for _ in range(H)]
    for i in range(H):
        row_a = grid_a[i]
        for j in range(H):
            if checked_b[j]:
                continue
            row_b = grid_b[j]
            if (sorted(row_a) == sorted(row_b)):
                checked_b[j] = True
                cnt_row = max(cnt_row, cnt_change(row_a, row_b))
                break

    if len([v for v in checked_b if v == False]):
        return -1

    cnt_col = 0
    checked_b = [False for _ in range(W)]
    for i in range(W):
        col_a = [row[i] for row in grid_a]
        for j in range(W):
            if checked_b[j]:
                continue
            col_b = [row[j] for row in grid_b]
            if (sorted(col_a) == sorted(col_b)):
                checked_b[j] = True
                cnt_col = max(cnt_col, cnt_change(col_a, col_b))
                break

    if len([v for v in checked_b if v == False]):
        return -1
    print(cnt_row, cnt_col)
    return cnt_row + cnt_col

H, W = map(int, input().split())
grid_a = [list(map(int, input().split())) for _ in range(H)]
grid_b = [list(map(int, input().split())) for _ in range(H)]
cnt = check()
print(cnt)
