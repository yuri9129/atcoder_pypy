from sys import stdin
readline = stdin.readline

# H行W列
# 連続Kマスがoであるか？
H, W, K = map(int, readline().split())

# マス目
# 読み込み行数が多くなるため、readline()で高速化
# 特定の文字の数を集計する必要があるが、list.count()が遅いためstr型で格納する
grids = [readline()[:-1] for _ in [0] * H]
# grids = [list(readline())[:-1] for _ in [0] * H]

# 横方向で探索
ret_x = []
ret_dot = []
for i in range(H):
    # 1行分のgridを取得
    l = grids[i]
    # K-1マス後ろまでにxマスが何マスあるかを累積和をカウント
    cnt_x = [0] * (W + 1)
    cnt_dot = [0] * (W + 1)
    for j in range(W):
        s, e = j-(K-1), j
        if(s < 0):
            s = 0
        target = l[j]
        if target == 'x':
            cnt_x[s] += 1
            cnt_x[e + 1] -= 1
        elif target == '.':
            cnt_dot[s] += 1
            cnt_dot[e + 1] -= 1

    for i in range(1, W):
        cnt_x[i] += cnt_x[i - 1]
        cnt_dot[i] += cnt_dot[i - 1]

    ret_x.append(cnt_x[:-(1 + K - 1)])
    ret_dot.append(cnt_dot[:-(1 + K - 1)])

ret = 10 ** 18
for i in range(H):
    for j in range(len(ret_x[i])):
        if ret_x[i][j] == 0 and ret > ret_dot[i][j]:
            ret = ret_dot[i][j]


# 縦方向で探索
grids2 = [''] * W
for i in range(H):
    for j in range(W):
        grids2[j] += grids[i][j]

ret_x = []
ret_dot = []

for i in range(W):
    # 1行分のgridを取得
    l = grids2[i]
    # K-1マス後ろまでにxマスが何マスあるかを累積和をカウント
    cnt_x = [0] * (H + 1)
    cnt_dot = [0] * (H + 1)
    for j in range(H):
        s, e = j-(K-1), j
        if(s < 0):
            s = 0
        target = l[j]
        if target == 'x':
            cnt_x[s] += 1
            cnt_x[e + 1] -= 1
        elif target == '.':
            cnt_dot[s] += 1
            cnt_dot[e + 1] -= 1

    for i in range(1, H):
        cnt_x[i] += cnt_x[i - 1]
        cnt_dot[i] += cnt_dot[i - 1]

    ret_x.append(cnt_x[:-(1 + K - 1)])
    ret_dot.append(cnt_dot[:-(1 + K - 1)])

for i in range(W):
    for j in range(len(ret_x[i])):
        if ret_x[i][j] == 0 and ret > ret_dot[i][j]:
            ret = ret_dot[i][j]


if ret == 10 ** 18:
    print(-1)
else:
    print(ret)