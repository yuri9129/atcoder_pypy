n = int(input())


results = [[False] * 100 for _ in range(100)]

for i in range(n):
    lx, rx, ly, ry = map(int, input().split())
    for x in range(lx, rx):
        for y in range(ly, ry):
            results[x][y] = True

cnt = 0
for lst in results:
    cnt += lst.count(True)

print(cnt)