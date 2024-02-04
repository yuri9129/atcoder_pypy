N = int(input())
lst = [input() for _ in range(N)]

for i, a in enumerate(lst):
    for j, b in enumerate(lst):
        if i == j:
            continue

        s = a + b
        if s == s[::-1]:
            print("Yes")
            exit()

print("No")
