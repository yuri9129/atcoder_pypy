
def decimal_to_binary(n):
    return bin(n)[2:]

n = int(input())
n2 = decimal_to_binary(n)

cnt = 0
for s in n2[::-1]:
    if s == '0':
        cnt += 1
    else:
        break

print(cnt)
