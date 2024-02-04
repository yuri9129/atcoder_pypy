n, l, r = map(int, input().split())

lst = list(map(int, input().split()))

ret = []
for a in lst:
    y_abs = 0
    if(not(l <= a <= r)):
        l_abs = abs(a - l)
        r_abs = abs(a - r)
        y_abs = min([l_abs, r_abs])
    if(l <= a - y_abs <= r):
        ret.append(a - y_abs)
    else:
        ret.append(a + y_abs)


print(" ".join(map(str, ret)))


