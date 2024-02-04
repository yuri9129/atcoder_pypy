N, Q = map(int, input().split())

queries = [list(map(str, input().split())) for _ in range(Q)]

positions = []

for i in range(N, 0, -1):
    positions.append([i, 0])

for query in queries:
    t, v = query
    if t == "1":
        # 移動する
        if v == "U":
            positions.append([positions[-1][0], positions[-1][1] + 1])
        elif v == "D":
            positions.append([positions[-1][0], positions[-1][1] - 1])
        elif v == "R":
            positions.append([positions[-1][0] + 1, positions[-1][1]])
        elif v == "L":
            positions.append([positions[-1][0] - 1, positions[-1][1]])

    elif t == "2":
        # パーツNの座標を出力
        print(f"{positions[int(v) * -1][0]} {positions[int(v) * -1][1]}")
