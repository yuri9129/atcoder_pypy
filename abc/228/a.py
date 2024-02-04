s, t, x = map(int, input().split())

if(s < t):
    print("Yes" if s <= x and x < t else "No")
else:
    s, t = t, s
    print("No" if s <= x and x < t else "Yes")
