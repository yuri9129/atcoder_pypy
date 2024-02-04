# N:頂点数
# M:辺数
N, M = map(int, input().split())

# nums: 各頂点の整数値
nums = list(map(int, input().split()))

edges = {}
for i in range(N):
    edges[i] = []

for _ in range(M):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    if nums[x] <= nums[y]:
        edges[x].append(y)
    if nums[y] <= nums[x]:
        edges[y].append(x)
max_point = 0

def dfs(i, visited):
    global max_point
    if i in visited:
        return

    visited.append(i)
    if i == N - 1:
        # print(visited, "->", [nums[v] for v in visited], "->", len(set([nums[v] for v in visited])))
        point = len(set([nums[v] for v in visited]))
        max_point = max(max_point, point)
        return
    for p in edges[i]:
        dfs(p, visited.copy())



dfs(0, [])

print(max_point)

