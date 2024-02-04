N, K = map(int, input().split())
lst = list(map(int, input().split()))

sum_diff = 0
if len(lst) % 2 == 0:
    for i in range(0, len(lst), 2):
        sum_diff += lst[i + 1] - lst[i]
    print(sum_diff)
    exit()

