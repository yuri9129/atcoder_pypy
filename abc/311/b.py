N, D = map(int, input().split())

lst = [list(input()) for _ in range(N)]
print(lst)

N, D = map(int, input().split())

lst = [list(input()) for _ in range(N)]
lst = [[(b == 'o') for b in a] for a in lst]
lst = [list(x) for x in zip(*lst)]

lst2 = [ all(x) for x in lst]


ret = 0
tmp = 0
for v in lst2:
    if v:
        tmp += 1
        ret = max(ret, tmp)
    else:
        tmp = 0

print(ret)