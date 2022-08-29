import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
ans = 0

for _ in range(m):
    a, b = map(int, input().split())

    graph[a].append(b)
    graph[b].append(a)

def bfs(v):
    visited[v] = True
    q = deque([v])

    while q:
        node = q.popleft()

        for i in graph[node]:
            if not visited[i]:
                visited[i] = True
                q.append(i)

for i in range(1, n + 1):
    if not visited[i]:
        bfs(i)
        ans += 1

print(ans)