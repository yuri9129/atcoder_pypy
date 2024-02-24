s = input()

l = {}

for v in list(s):
    if v not in l:
        l[v] = 0

    l[v] += 1

for k, v in l.items():
    if v == 1:
        se = k

for i in range(len(s)):
    if s[i] == se:
        print(i + 1)

