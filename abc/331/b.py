N, S, M, L = map(int, input().split())

# s:6, m:8, l:12

cnt_s = 0
cnt_m = 0
cnt_l = 0
price = 9999999999999999

def get_price(s, m, l):
    return s * S + m * M + l * L

for s in range((N // 6) + 2):
    for m in range((N // 8) + 2):
        for l in range((N // 12) + 2):
            if((s * 6 + m * 8 + l * 12) >= N):
                price = min(price, get_price(s, m, l))


print(price)