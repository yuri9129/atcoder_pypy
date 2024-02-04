# n: 人数
# k: カードの枚数
# a: a人目から配り始める
n, k, a = map(int, input().split())

ret = ((a - 1) + k - 1) % n + 1
print(ret)
