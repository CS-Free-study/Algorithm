from collections import deque

# 기존 코드
#
# def solution(priorities, location):
#     q = deque(priorities)
#     n = deque(range(len(priorities)))
#     ans = 0

#     while True:
#         if q[0] == max(q):
#             q.popleft()
#             num = n.popleft()
#             ans += 1

#             if num == location:
#                 return ans
#         else:
#             q.append(q.popleft())
#             n.append(n.popleft())

# 개선된 코드

def solution(priorities, location):
    q = deque((i, p) for i, p in enumerate(priorities))
    ans = 0
    
    while True:
        n = q.popleft()
        if any(n[1] < v[1] for v in q):
            q.append(n)
        else:
            ans += 1
            if n[0] == location:
                return ans