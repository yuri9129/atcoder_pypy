from sortedcontainers import SortedSet



n, q = map(int, input().split())
a_lst = list(map(int, input().split()))

# ss = SortedSet([x for x in range(n + 1)])

cnt_lst = [0] * (n + 1)
for a in a_lst:
    if(a <= n):
        cnt_lst[a] += 1

no_lst = []
for k, v in enumerate(cnt_lst):
    if(v == 0):
        no_lst.append(k)
ss = SortedSet(no_lst)

ans = []
for _ in range(q):
    idx, v = map(int, input().split())
    idx -= 1
    a = a_lst[idx]
    a_lst[idx] = v
    if(a <= n):
        cnt_lst[a] -= 1
        if(cnt_lst[a] == 0):
            ss.add(a)

    if(v <= n):
        cnt_lst[v] += 1
        if(cnt_lst[v] == 1):
            ss.remove(v)

    ans.append(ss[0])

print(*ans, sep="\n")



