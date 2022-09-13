# Level 2

from heapq import heappush, heappop, heapify

def solution(scoville, K):
    ans = 0
    heapify(scoville)

    while scoville[0] < k:
        heappush(scoville, heappop(scoville) + heappop(scoville) * 2)
        ans += 1
        if len(scoville) == 1 and scoville[0] < k:
            return -1
        
    return ans

s = [1, 2, 3, 9, 10, 12]
k = 7
print(solution(s, k))