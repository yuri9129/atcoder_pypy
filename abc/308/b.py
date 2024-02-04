N, M = map(int, input().split())

lst = list(input().split())


a = list(input().split())
b = list(map(int, input().split()))

other_price = b[0]
b = b[1:]
prices = dict(zip(a, b))

ret = 0
for v in lst:
    if v in prices:
        ret += prices[v]
    else:
        ret += other_price

print(ret)

