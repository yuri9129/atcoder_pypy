# import time
# start_time = time.time()

from sys import stdin
readline = stdin.readline

N = int(input())
S = input()
Q = int(input())
# print(f"Elapsed time: {time.time() - start_time} seconds")
char_list = {}
for x in 'abcdefghijklmnopqrstuvwxyz':
    char_list[x] = [x]


# print(f"Elapsed time: {time.time() - start_time} seconds")

# for i in range(N):
#     v = S[i]
#     if v not in char_list:
#         char_list[v] = []
#     char_list[v].append(i)
# print(f"Elapsed time: {time.time() - start_time} seconds")




for _ in range(Q):
    before_str, after_str = readline()[:-1].split()
    if after_str == before_str:
        continue

    char_list[after_str] += char_list[before_str]
    char_list[before_str] = []
# print(f"Elapsed time: {time.time() - start_time} seconds")

mappings = {}
for after_char, lst in char_list.items():
    for before_char in lst:
        mappings[before_char] = after_char
# print(f"Elapsed time: {time.time() - start_time} seconds")

ret = ''
for v in S:
    ret += mappings[v]

print(ret)
# print(f"Elapsed time: {time.time() - start_time} seconds")

