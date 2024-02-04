n = int(input())
lst = list(map(int, input().split()))

cnt = 0
for month, max_day in enumerate(lst):
    month += 1
    for day in range(1, max_day + 1):
        myset = set()
        for v in list(str(month)):
            myset.add(v)
        for v in list(str(day)):
            myset.add(v)

        if len(myset) == 1:
            cnt += 1
print(cnt)
