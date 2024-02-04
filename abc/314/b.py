n = int(input())
lst = []
for i in range(n):
    lst.append([int(input()), list(map(int, input().split()))])
x = int(input())

ok_lst = []
for i in range(n):
    if x in lst[i][1]:
        ok_lst.append([i, lst[i][0]])


if len(ok_lst) == 0:
    print("0")
    exit()

min_num = min(list(a[1] for a in ok_lst))
ret = []

for player, num in ok_lst:
    if num == min_num:
        ret.append(player + 1)


ret.sort()
print(len(ret))
print(" ".join(map(str, ret)))