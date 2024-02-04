N = int(input())
nums = list(map(int, input().split()))

min_ret = 0
sum_ret = 0
for n in nums:
    sum_ret += n
    min_ret = min(min_ret, sum_ret)

print((min_ret * -1) + sum_ret)

