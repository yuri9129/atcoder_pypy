M, D = map(int, input().split())

y, m, d = map(int, input().split())


ans_y = 0
ans_m = 0
ans_d = 0

ans_d = d + 1
if(d == D):
    m += 1
    ans_d = 1

ans_m = m
if(m > M):
    y += 1
    ans_m = 1

ans_y = y

print(f"{ans_y} {ans_m} {ans_d}")