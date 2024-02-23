Q = int(input())
queries = [list(map(str, input().split())) for _ in range(Q)]

lst = []
for query in queries:
    num, val = query
    val = int(val)
    if num == '1':
        lst.append(val)
    else:
        print(lst[-1 * val])