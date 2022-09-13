# Level 3

from heapq import heappush, heappop

def solution(operations):
    h = []
    ans = [0, 0]

    for operation in operations:
        op = list(operation.split())
        if op[0] == 'I':
            heappush(h, int(op[1]))
        elif h:
            if op[1] == '1':
                h = h[:-1]
            else:
                heappop(h)
    
    if h:
        ans[0], ans[1] = max(h), min(h)
    
    return ans

# o = ["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]
# o = ["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]
o = ["I -1", "I -10", "I -15", "I 60", "D -1", "D 1"]
print(solution(o))