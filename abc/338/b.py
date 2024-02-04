s = input()

l = {}
for v in list(s):
    if v not in l:
        l[v] = 0
    l[v] += 1

l2 = []
for k, v in l.items():
    l2.append((-v, k))


l2.sort()
print(l2[0][1])