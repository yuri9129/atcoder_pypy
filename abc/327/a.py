n = int(input())
lst = list(input())

for i in range(n - 1):
    myset = set()
    myset.add(lst[i])
    myset.add(lst[i + 1])
    if('a' in myset and 'b' in myset):
        print('Yes')
        exit()

print("No")
