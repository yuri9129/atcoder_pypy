# N:日数
# M:無地Tの枚数
N, M = map(int, input().split())

S = input().split("0")

ret = 0
for s in S:
    events = list(s)

    event1 = len([v for v in events if v == '1'])
    event2 = len([v for v in events if v == '2'])

    a = max(event1 - M, 0)
    ret = max(a + event2, ret)


print(ret)
