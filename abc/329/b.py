n = int(input())

lst = list(map(int, input().split()))
nums = list(set(lst))
nums.sort()
print(nums[-2])

