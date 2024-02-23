import math

def lcm(a, b):
    return a * b // math.gcd(a, b)

N, M, K = map(int, input().split())

# この値以下に答えがあるはず。
tmp_max = max(N, M) * K

# この値以上に答えがあるはず。
tmp_min = 0

# 二分探索
while tmp_max - tmp_min > 1:
    mid = (tmp_max + tmp_min) // 2
    r = (mid // N) + (mid // M) - 2 * (mid // lcm(N, M))

    if r == K:
        cnt = 0
        if (mid % N) == 0:
            cnt += 1
        if (mid % M) == 0:
            cnt += 1
        if cnt == 1:
            print(mid)
            exit()

    if r < K:
        tmp_min = mid
    else:
        tmp_max = mid

    # print(tmp_min, tmp_max, mid, r)


if (tmp_max // N) + (tmp_max // M) - 2 * (tmp_max // (N * M)) == K:
    print(tmp_max)
else:
    print(tmp_min)