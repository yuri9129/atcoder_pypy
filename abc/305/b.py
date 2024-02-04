d = [3,1,4,1,5,9]
l = {v:k for k, v in enumerate("ABCDEFG")}

a, b = input().split()
a = l[a]
b = l[b]
start = min(a, b)
end = max(a, b)

ret = 0
for i in range(start, end):
    ret += d[i]

print(ret)