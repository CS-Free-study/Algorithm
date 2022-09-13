# Level 3

from heapq import heappush, heappop

def solution(jobs):
    h = []
    prev_start = -1
    now = ans = cnt = 0

    while cnt < len(jobs):
        for job in jobs:
            if prev_start < job[0] <= now:
                heappush(h, (job[1], job[0]))
        if h:
            job = heappop(h)
            prev_start = now
            now += job[0]
            ans += now - job[1]
            cnt += 1
        else:
            now += 1

    return ans // len(jobs)

jobs = [[0, 3], [1, 9], [2, 6]]
print(solution(jobs))