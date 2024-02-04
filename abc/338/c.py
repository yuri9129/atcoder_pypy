N = int(input())

heights = list(map(int, input().split()))

plan_a = list(map(int, input().split()))
plan_b = list(map(int, input().split()))



def my_process():
    max_cnt = 0
    for cnt_a in range(999999999):
        h = heights[:]
        max_b = 999999999999
        for i in range(N):
            h[i] -= plan_a[i] * cnt_a
            if h[i] < 0:
                return max_cnt
            if plan_b[i] > 0:
                max_b = min(max_b, h[i] // plan_b[i])
        max_cnt = max(max_cnt, cnt_a + max_b)

    return max_cnt

ret = my_process()

print(ret)
