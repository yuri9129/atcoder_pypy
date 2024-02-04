S = list(input())

prev_s = S.pop(0)
for s in S:
    if prev_s > s:
        print("No")
        exit()
    prev_s = s
print("Yes")