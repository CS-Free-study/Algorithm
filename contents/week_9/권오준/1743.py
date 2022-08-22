import sys
from collections import deque
input = sys.stdin.readline

n, m, k = map(int, input().split())
graph = [[0] * m for _ in range(n)]
visited = [[0] * m for _ in range(n)]
q = deque()
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
ans = []

for _ in range(k):
    a, b = map(int, input().split())

    graph[a - 1][b - 1] = 1

def bfs(x, y):
    q.append((x, y))
    visited[x][y] = 1
    cnt = 0

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y

            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0 and graph[nx][ny] == 1:
                visited[nx][ny] = 1
                q.append((nx, ny))
                cnt += 1
    
    ans.append(cnt)


for i in range(n):
    for j in range(m):
        if graph[i][j] == 1 and visited[i][j] == 0:
            bfs(i, j)

print(max(ans) + 1)