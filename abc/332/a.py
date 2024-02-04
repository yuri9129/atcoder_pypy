N, S, K = map(int, input().split())

total_price = 0
for _ in range(N):
    price, quantity = map(int, input().split())
    total_price += price * quantity

if total_price < S:
    total_price += K
print(total_price)