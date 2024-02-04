n = int(input())

lst = list(map(int, input().split()))

nums_lst = {}

for v in lst:
    if(v in nums_lst):
        nums_lst[v] += 1
    else:
        nums_lst[v] = 1

nums_lst = dict(sorted(nums_lst.items(), key=lambda x:x[0], reverse=True) )

ret = {}
num_sum = 0
for v, cnt in nums_lst.items():
    ret[v] = num_sum
    num_sum += cnt * v

ret2 = []
for v in lst:
    ret2.append(ret[v])

print(" ".join(map(str, ret2)))
