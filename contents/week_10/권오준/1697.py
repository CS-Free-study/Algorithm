import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [0] * 100001

def bfs():
    q = deque([n])
    
    while q:
        x = q.popleft()

        if x == m:
            return graph[x]
        
        for i in (x - 1, x + 1, x * 2):
            if 0 <= i < 100001 and graph[i] == 0:
                graph[i] = graph[x] + 1
                q.append(i)

print(bfs())  