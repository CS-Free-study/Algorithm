import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
ans = []

for _ in range(m):
    a, b = map(int, input().split())

    graph[b].append(a)

def bfs(v):
    visited = [False] * (n + 1)
    visited[v] = True
    q = deque([v])
    cnt = 1

    while q:
        v = q.popleft()

        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                cnt += 1
                q.append(i)
    
    return cnt

for i in range(1, n + 1):
    ans.append(bfs(i))

maxValue = max(ans)
for i in range(n):
    if ans[i] == maxValue:
        print(i + 1, end = ' ')