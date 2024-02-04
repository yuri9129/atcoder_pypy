N = int(input())

takahashi = 0
aoki = 0
for _ in range(N):
    p1, p2 = map(int, input().split())
    takahashi += p1
    aoki += p2

if takahashi > aoki:
    print("Takahashi")
elif takahashi < aoki:
    print("Aoki")
else:
    print("Draw")