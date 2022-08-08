import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
ans = []
maxValue = 0

for _ in range(m):
    a, b = map(int, input().split())
    graph[b].append(a)

def bfs(v):
    q = deque([v])
    visited = [0] * (n + 1)
    visited[v] = 1
    cnt = 1

    while q:
        node = q.popleft()
        for i in graph[node]:
            if visited[i] == 0:
                visited[i] = 1
                cnt += 1
                q.append(i)

    return cnt

for i in range(1, n + 1):
    cnt = bfs(i)
    if cnt == maxValue:
        ans.append(i)
    if cnt > maxValue:
        maxValue = cnt
        ans.clear()
        ans.append(i)

print(" ".join(map(str, ans)))