import sys
from collections import deque
input = sys.stdin.readline

def bfs(z, x, y):
    q = deque([(z, x, y)])
    visited[z][x][y] = True

    while q:
        z, x, y = q.popleft()

        for i in range(6):
            nz = dz[i] + z
            nx = dx[i] + x
            ny = dy[i] + y

            if 0 <= nz < l and 0 <= nx < r and 0 <= ny < c and not visited[nz][nx][ny] and graph[nz][nx][ny] != '#':
                ans[nz][nx][ny] = ans[z][x][y] + 1
                q.append((nz, nx, ny))
                visited[nz][nx][ny] = True

while True:
    l, r, c = map(int, input().split())
    if l == 0:
        break

    graph = [[] * r for _ in range(l)]
    visited = [[[False] * c for _ in range(r)] for _ in range(l)]
    ans = [[[0] * c for _ in range(r)] for _ in range(l)]
    dx = [-1, 1, 0, 0, 0, 0]
    dy = [0, 0, -1, 1, 0, 0]
    dz = [0, 0, 0, 0, -1, 1]

    for i in range(l):
        for _ in range(r):
            graph[i].append(list(map(str, input().rstrip())))
        input()

    for i in range(l):
        for j in range(r):
            for k in range(c):
                if graph[i][j][k] == 'S':
                    sz, sx, sy = i, j, k
                if graph[i][j][k] == 'E':
                    ez, ex, ey = i, j, k
    
    bfs(sz, sx, sy)
    print("Trapped!") if ans[ez][ex][ey] == 0 else print(f"Escaped in {ans[ez][ex][ey]} minute(s).")