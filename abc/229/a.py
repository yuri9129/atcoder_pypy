def get(x, y):
    global lst
    return lst[y][x]


lst = [list(input()) for _ in range(2)]

if((get(1,0) == '.' and get(0, 1) == '.') or (get(1, 1) == '.' and get(0,0) == '.')):
    print("No")
else:
    print("Yes")