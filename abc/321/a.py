lst = list(map(int, list(input())))

for i in range(len(lst) - 1):
    if lst[i] <= lst[i + 1]:
        print("No")
        exit()

print("Yes")