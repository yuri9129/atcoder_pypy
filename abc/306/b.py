lst = list(map(int, input().split()))

a = 0
ret = 0
for v in lst:
    ret += v * (2 ** (a))
    a += 1
print(ret)