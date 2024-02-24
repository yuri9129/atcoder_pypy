N = int(input())
p_lst = list(map(int, input().split()))

dic = {}
for i in range(N):
    dic[p_lst[i]] = i


Q = int(input())

for _ in range(Q):
    a, b = map(int, input().split())

    if dic[a] < dic[b]:
        print(a)
    else:
        print(b)