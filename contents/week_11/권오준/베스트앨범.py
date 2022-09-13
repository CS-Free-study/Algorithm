# Level 3

from collections import defaultdict

def solution(genres, plays):
    d = defaultdict(list)
    ans = []

    for i in range(len(genres)):
        d[genres[i]].append(plays[i])

    d = dict(sorted(d.items(), key = lambda x: sum(x[1]), reverse = True))

    for k, v in d.items():
        v.sort(reverse = True)
        cnt = 0

        for i in v:
            if cnt == 2:
                break
            for j in range(len(genres)):
                if plays[j] == i and genres[j] == k:
                    ans.append(j)
                    cnt += 1
            
    return ans