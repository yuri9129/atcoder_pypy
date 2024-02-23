N = int(input())
coins = list(map(int, input().split()))

rates = [list(map(int, input().split())) for _ in range(N-1)]

for i in range(N-1):
    coin = coins[i]
    rate_from = rates[i][0]
    rate_to = rates[i][1]

    cnt = coin // rate_from
    coins[i] -= rate_from * cnt
    coins[i+1] += rate_to * cnt

print(coins[-1])


