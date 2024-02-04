N, M = list(map(int, input().split()))
tours = list(map(int, input().split()))

lst = [0] * N
prev = tours[0] - 1
for current in tours[1:]:
    current -= 1
    # print(f"{prev}->{current}")
    # d = abs(current - prev)
    # if d == M / 2:
    #     print(lst)
    #     continue
    # print(f"abs(current - prev): {abs(current - prev)}")
    # print(f"abs(max(current, prev) - min(current, prev) + N): {abs(max(current, prev) - (min(current, prev) + N))}")
    if abs(current - prev) < abs(max(current, prev) - (min(current, prev) + N)):
        lst[min(current, prev)] += 1
        lst[max(current, prev)] -= 1
        # for v in range(min(current, prev), max(current, prev)):
        #     lst[v] += 1
    elif abs(current - prev) > abs(max(current, prev) - (min(current, prev) + N)):
        lst[max(current, prev)] += 1
        lst[0] += 1
        lst[(min(current, prev) + N) % N] -= 1
        # for v in range(max(current, prev), min(current, prev) + N):
        #     lst[v % N] += 1

    prev = current
    # print(lst)

# print(lst)
lst2 = []
prev = 0
for v in lst:
    lst2.append(prev + v)
    prev = lst2[-1]
# print(lst2)
# print(lst)
bridge = None
num = 999999999999
for k, v in enumerate(lst2):
    if v < num:
        num = v
        bridge = k
# print(lst2)
# print(bridge)

prev = tours[0] - 1
d_sum = 0
for current in tours[1:]:
    current -= 1
    a = (min(current, prev) + N - 1 - bridge) % N
    b = (max(current, prev) + N - 1 - bridge) % N


    # print(a, b)
    # print(abs(a - b))
    # print(abs(max(a, b) - (min(a, b) + N)))
    # d = min(abs(a - b), abs(max(a, b) - (min(a, b) + N)))
    d = abs(a - b)

    d_sum += d
    # print(f"{prev}->{current} : {d}")

    prev = current

print(d_sum)