n = int(input())

div_2 = 0
div_3 = 0
while(n % 2 == 0):
    n = n // 2
    div_2 += 1
while(n % 3 == 0):
    n = n // 3
    div_3 += 1
if(n == 1):
    print("Yes")
else:
    print("No")
