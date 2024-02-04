N = int(input())

lst = list(map(int, input().split()))
dic = {}
for k, v in enumerate(lst):
    dic[v] = k + 1


ret = [dic[-1]]

while(True):
    if ret[-1] not in dic:
        break
    ret.append(dic[ret[-1]])
print(" ".join(map(str, ret)))