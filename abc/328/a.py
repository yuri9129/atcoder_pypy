n, x = map(int, input().split())
scores = list(map(int, input().split()))

sum = 0
for score in scores:
    if score <= x:
        sum += score

print(sum)