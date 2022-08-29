import sys
from collections import deque
input = sys.stdin.readline

n, m, k = map(int, input().split())
graph = [[0] * m for _ in range(n)]
vistied = [[False] * m for _ in range(n)]
q = deque()
dx = [-1, 1, 0 ,0]
dy = [0, 0, -1, 1]
ans = []

for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())

    for x in range(y1, y2):
        for y in range(x1, x2):
            graph[x][y] = 1

def bfs(x, y):
    vistied[x][y] = True
    q.append((x, y))
    cnt = 1

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y

            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0 and not vistied[nx][ny]:
                cnt += 1
                vistied[nx][ny] = True
                q.append((nx, ny))
    
    ans.append(cnt)

for x in range(n):
    for y in range(m):
        if graph[x][y] == 0 and not vistied[x][y]:
            bfs(x, y)

ans.sort()

print(len(ans))
print(*ans)