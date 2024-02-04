N = int(input())

for a in range(0, N + 1):
    for b in range(0, N + 1):
        for c in range(0, N + 1):
            if(a + b + c <= N):
                print(f"{a} {b} {c}")



