N, M = map(int, input().split())
X = list(map(int, input().split()))

d = [0] * (N + 1)
for i in range(M - 1):
    l, r = min(X[i], X[i + 1]), max(X[i], X[i + 1])
    d[1] += r - l
    d[l] += N - (r - l) - (r - l)
    d[r] += r - 1 - (N - (r - 1))
    print(d)

ans = 10 ** 18
for i in range(1, N + 1):
    d[i] += d[i - 1]
    ans = min(ans, d[i])
print(d)
print(ans)