n = int(input())

lst = [list(input()) for _ in range(n)]

i_lst = []
for i in range(n):
    cnt = 0
    for j in range(n):
        if lst[i][j] == "o":
            cnt += 1
    i_lst.append(cnt)

j_lst = []
for j in range(n):
    cnt = 0
    for i in range(n):
        if lst[i][j] == "o":
            cnt += 1
    j_lst.append(cnt)


ans = 0
for i, cnt_i in enumerate(i_lst):
    for j, cnt_j in enumerate(j_lst):
        if lst[i][j] != "o":
            continue
        ans += (cnt_i - 1) * (cnt_j - 1)

print(ans)

