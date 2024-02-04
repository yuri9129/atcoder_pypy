import math
d = int(input())

# 探索するxの最大値
x_max = math.ceil(math.sqrt(d))

ret_min = 10 ** 12
positions = [0,0]
for x in range(x_max + 1):
    diff = x ** 2 - d
    if(diff > 0):
        y = 0
        ret = diff
    else:
        y1 = math.floor(math.sqrt(abs(x **2 - d)))
        ret1 = abs(y1 ** 2 + diff)
        y2 = math.ceil(math.sqrt(abs(x **2 - d)))
        ret2 = abs(y2 ** 2 + diff)
        if(ret1 < ret2):
            y = y1
            ret = ret1
        else:
            y = y2
            ret = ret2
    if ret_min > ret:
        ret_min = ret
        positions = [x, y]

print(ret_min)
# print(positions)
