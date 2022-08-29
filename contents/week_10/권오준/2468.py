import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
max_height = 1
ans = 0

def bfs(x, y, h):
    global ans
    q = deque()
    q.append((x, y))
    visited[x][y] = True

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y

            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] > h and not visited[nx][ny]:
                visited[nx][ny] = True
                q.append((nx, ny))
        

for i in graph:
    max_height = max(i)

for i in range(max_height):
    visited = [[False] * n for _ in range(n)]
    cnt = 0
    for x in range(n):
        for y in range(n):
            if graph[x][y] > i and not visited[x][y]:
                bfs(x, y, i)
                cnt += 1

    ans = max(cnt, ans)

print(ans)
