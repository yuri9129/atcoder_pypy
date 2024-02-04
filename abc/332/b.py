K, G, M = map(int, input().split())

glass = 0
cup = 0

for _ in range(K):
    if glass == G:
        glass = 0
        continue
    if cup == 0:
        cup = M
        continue
    # グラスに入れられる残り
    less = G - glass
    if less < cup:
        glass += less
        cup -= less
    else:
        glass += cup
        cup = 0

print(f"{glass} {cup}")
