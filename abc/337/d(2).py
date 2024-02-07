from sys import stdin
readline = stdin.readline

# H行W列
# 連続Kマスがoであるか？
H, W, K = map(int, readline().split())

# マス目
# 読み込み行数が多くなるため、readline()で高速化
grids = [list(readline())[:-1] for _ in [0] * H]


# 横方向で探索
# (操作回数, oが連続する回数)
# (2, 3) は、.->oの変換2回操作したときに3マス連続でoがある
h_ans = [[(0, 0)] * W for _ in [0] * H]
for i in range(H):
    for j in range(W):
        v = grids[i][j]
        if j == 0:
            prev_cnt, prev_op = 0, 0
        else:
            prev_cnt, prev_op = h_ans[i][j - 1]

        if v == '.':
            # .->oの変換を1回行い、oの連続数を+1する
            h_ans[i][j] = (prev_cnt + 1, prev_op + 1)
        elif v == 'o':
            # 変換は行わず、oの連続数を+1する
            h_ans[i][j] = (prev_cnt, prev_op + 1)
        # v == 'x' の場合は何もせず(0,0)とする

# 縦方向で探索
v_ans = [[(0, 0)] * W for _ in [0] * H]
for j in range(W):
    for i in range(H):
        v = grids[i][j]
        if i == 0:
            prev_cnt, prev_op = 0, 0
        else:
            prev_cnt, prev_op = v_ans[i - 1][j]

        if v == '.':
            # .->oの変換を1回行い、oの連続数を+1する
            v_ans[i][j] = (prev_cnt + 1, prev_op + 1)
        elif v == 'o':
            # 変換は行わず、oの連続数を+1する
            v_ans[i][j] = (prev_cnt, prev_op + 1)
        # v == 'x' の場合は何もせず(0,0)とする


for v in h_ans:
    print(v)

print("===")
for v in v_ans:
    print(v)

ret = 10 ** 18
for l in h_ans:
    for cnt, op in l:
        if op >= K and (cnt - (op - K)) < ret:
            if(cnt - (op - K)) > 0:
                ret = (cnt - (op - K))
            else:
                ret = 0

for l in v_ans:
    for cnt, op in l:
        if op >= K and (cnt - (op - K)) < ret:
            if(cnt - (op - K)) > 0:
                ret = (cnt - (op - K))
            else:
                ret = 0

if ret == 10 ** 18:
    print(-1)
else:
    print(ret)