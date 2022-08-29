import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
graph = [list(map(str, input().rstrip())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
ans = [0, 0]

def bfs(x, y):
    visited[x][y] = True
    q = deque([(x, y)])
    color = graph[x][y]

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y

            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and graph[nx][ny] == color:
                visited[nx][ny] = True
                q.append((nx, ny))

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i, j)
            ans[0] += 1

visited = [[False] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if graph[i][j] == 'G':
            graph[i][j] = 'R'

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i, j)
            ans[1] += 1

print(*ans)