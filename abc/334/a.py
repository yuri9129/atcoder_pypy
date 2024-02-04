A, K, S, E = map(int, input().split())

S -= A
E -= A

print(E // K - (S - 1) // K)
