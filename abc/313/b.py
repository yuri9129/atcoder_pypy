n, m = map(int, input().split())

# 最強の可能性があるプレイヤー一覧
players = set([i for i in range(1, n+1)])

for _ in range(m):
    winner, loser = map(int, input().split())
    players.discard(loser)

if len(players) == 1:
    print(players.pop())
else:
    print("-1")

