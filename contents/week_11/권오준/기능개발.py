from collections import deque

def solution(progresses, speeds):
    pro_q, sp_q = deque(progresses), deque(speeds)
    ans = []
    cnt = 0
    day = 1
    
    while pro_q:
        if pro_q[0] + day * sp_q[0] >= 100:
            pro_q.popleft()
            sp_q.popleft()
            cnt += 1
        else:
            if cnt:
                ans.append(cnt)
            cnt = 0
            day += 1
    
    ans.append(cnt)
    
    return ans
	
p = [95, 90, 99, 99, 80, 99]
s = [1, 1, 1, 1, 1, 1]
print(solution(p, s))
    