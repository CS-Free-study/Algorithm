import sys
from collections import deque
input = sys.stdin.readline

f, s, g, u, d = map(int, input().split())
graph = [0] * (f + 1)
visited = [False] * (f + 1)

def bfs():
    q = deque([s])
    visited[s] = True

    while q:
        n = q.popleft()

        if n == g:
            return graph[g]
        
        for i in (n + u, n - d):
            if 0 < i <= f and not visited[i]:
                visited[i] = True
                graph[i] = graph[n] + 1
                q.append(i)
    
    if graph[g] == 0:
        return "use the stairs"

print(bfs())