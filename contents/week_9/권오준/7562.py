import sys
from collections import deque
inpu = sys.stdin.readline

def bfs(x, y):
    q = deque([(x, y)])
    
    while q:
        x, y = q.popleft()

        for i in range(8):
            nx = dx[i] + x
            ny = dy[i] + y

            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                q.append((nx, ny))

for _ in range(int(input())):
    n = int(input())
    sy, sx = map(int, input().split())
    ey, ex = map(int, input().split()) 
    graph = [[0] * n for _ in range(n)]
    dx = [-1, -1, 1, 1, -2, -2, 2, 2]
    dy = [-2, 2, -2, 2, -1, 1, -1, 1]

    if sx == ex and sy == ey:
        print(0)
        continue

    bfs(sx, sy)
    print(graph[ex][ey])