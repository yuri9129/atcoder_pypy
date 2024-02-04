n = int(input())

lst = list(map(int, input().split()))

min_num = min(lst)
max_num = max(lst)

for i in range(min_num, max_num + 1):
    if i not in lst:
        print(i)
        exit()
