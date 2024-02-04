n, x = map(int, input().split())

scores = list(map(int, input().split()))

def get_score(scores):
    ret = sum(scores) - max(scores) - min(scores)
    return ret


ret = -1
for i in range(100 + 1):
    current_scores = list(scores)
    current_scores.append(i)
    if(get_score(current_scores) >= x):
        ret = i
        break


print(ret)