import sys
from collections import deque
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    s = list(input().rstrip().split())
    q = deque(s[0])
    
    for i in range(1, n):
        if s[i] <= q[0]:
            q.appendleft(s[i])
        else:
            q.append(s[i])
    
    print(''.join(q))