s = input()

def is_kaibun(s):
    if s == s[::-1]:
        return True
    else:
        return False

ret = 0
for i in range(0, len(s)):
    for j in range(i + 1, len(s) + 1):
        if is_kaibun((s[i:j])):
            ret = max(ret, len(s[i:j]))
print(ret)
