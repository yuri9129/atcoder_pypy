n = int(input())

lst = [list(input()) for _ in range(n)]


# player_1がplayer_2に勝ったかどうか
def get_result(player_1, player_2):
    return lst[player_1][player_2]

# player_1の勝利数
def get_wins(player_1):
    cnt = 0
    for v in lst[player_1]:
        if v == 'o':
            cnt += 1
    return cnt

ret = []
for i in range(n):
    # [player_1の勝利数, player_1の番号]
    ret.append([get_wins(i) * -1, i])

ret.sort()

print_out = [ret_i[1] + 1 for ret_i in ret]

print(*print_out, sep=" ")