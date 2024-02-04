n, l = map(int, input().split())
lst = list(map(int, input().split()))

cnt = 0
for v in lst:
    if v >= l:
        cnt += 1

print(cnt)
