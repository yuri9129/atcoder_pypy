x = int(input())

if(x == 1):
    print(1)
    exit()

for i in range(2, 17):
    b = x
    cnt = 0
    while(b % i == 0):
        b //= i
        cnt += 1

    if(b == 1 and cnt == i):
        print(i)
        exit()


print(-1)

