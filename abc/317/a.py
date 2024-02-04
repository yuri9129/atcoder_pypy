n, h, x = map(int, input().split())

lst = list(map(int, input().split()))

for k, v in enumerate(lst):
    if (h + v) >= x:
        print(k + 1)
        exit()

