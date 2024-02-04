n = int(input())

lst = []
for i in range(n):
    w, x = list(map(int, input().split()))
    lst.append([w, x])

max = -1
max_time = -1
for hour in range(24):
    cnt = 0
    for(people, time_diff) in lst:
        if 9 <= ((hour + time_diff) % 24) < 18:
            cnt += people
    if max < cnt:
        max = cnt
        max_time = hour

print(max)


