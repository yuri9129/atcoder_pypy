n = int(input())

def is326(num):
    nums = list(map(int, list(str(num))))
    if nums[0] * nums[1] == nums[2]:
        return True
    return False


while(True):
    if is326(n):
        print(n)
        exit()
    n += 1
