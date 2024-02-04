n, m = map(int, input().split())
s = input()
t = input()

ret = 3

if(t[:n] == s):
    ret -= 2
if(t[-n:] == s):
    ret -= 1

print(ret)