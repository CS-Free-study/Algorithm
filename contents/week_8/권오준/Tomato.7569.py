# 백준 7569, 토마토, 골드5
import sys
from collections import deque
input = sys.stdin.readline

m, n, h = map(int, input().split())
graph = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]
q = deque()
dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]
ans = 0

for z in range(h):
    for x in range(n):
        for y in range(m):
            if graph[z][x][y] == 1:
                q.append((x, y, z))

def bfs():
    while q:
        x, y, z = q.popleft()

        for i in range(6):
            nx = dx[i] + x
            ny = dy[i] + y
            nz = dz[i] + z
            
            if 0 <= nx < n and 0 <= ny < m and 0 <= nz < h and graph[nz][nx][ny] == 0:
                graph[nz][nx][ny] = graph[z][x][y] + 1
                q.append((nx, ny, nz))

bfs()
for z in range(h):
    for x in range(n):
        for y in range(m): 
            if graph[z][x][y] == 0:
                print(-1)
                exit()
            ans = max(ans, graph[z][x][y])

print(ans - 1)