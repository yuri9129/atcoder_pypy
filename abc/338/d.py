# N: 島の数
# M: 移動する島の数
N, M = map(int, input().split())

# 移動する島のリスト
tours = list(map(lambda x: int(x) - 1, input().split()))

# dist[i]: 島iから島i+1を封鎖したときの総移動距離
dist = [0] * N
for i in range(M - 1):
    # 島aから島bへ移動する場合
    a, b = tours[i], tours[i + 1]

    if a > b:
        # a < b になるように入れ替える
        a, b = b, a

    # 島xから島x+1の橋を封鎖したときの移動距離をdistに加算
    d1 = b - a
    d2 = N - (b - a)
    dist[0] += d1
    dist[a] += d2 - d1
    dist[b] += d1 - d2
    # dist[a] += N - (b - a)
    # dist[b + 1] -= N -(b - a)
    # for x in range(N):
    #     if a <= x < b:
    #         dist[x] += N - (b - a)
    #     else:
    #         dist[x] += b - a

# 累積和を取る
for i in range(1, N):
    dist[i] += dist[i - 1]

print(min(dist))

