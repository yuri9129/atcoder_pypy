N, D = map(int, input().split())

lst = []
for _ in range(N):
    i = list(map(int, input().split()))
    lst.append([
        i[0],
        i[1],
        i[2:]
    ])

for p1 in lst:
    for p2 in lst:
        if p1 == p2:
            continue
        if not(p1[0] >= p2[0]):
            continue
        if not(all( v in p2[2] for v in p1[2])):
            continue
        if not(p1[0] > p2[0] or p1[1] < p2[1]):
            continue
        print("Yes")
        exit()

print("No")
