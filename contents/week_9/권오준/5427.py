from collections import deque
import sys
input = sys.stdin.readline

def bfs():
    while q:
        x, y = q.popleft()

        if visited[x][y] == -999:
            isFire = True
        else:
            isFire = False

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < m and 0 <= ny < n:
                if visited[nx][ny] == -1 and (
                    graph[nx][ny] == "." or graph[nx][ny] == "@"
                ):
                    if isFire:
                        visited[nx][ny] = -999
                    else:
                        visited[nx][ny] = visited[x][y] + 1
                    q.append((nx, ny))
            else:
                if not isFire:
                    return visited[x][y] + 1

    return "IMPOSSIBLE"

for _ in range(int(input())):
    n, m = map(int, input().split())
    q = deque()
    graph = []
    visited = [[-1] * n for _ in range(m)]
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]

    for i in range(m):
        graph.append(list(input().strip()))
        for j in range(n):
            if graph[i][j] == "@":
                visited[i][j] = 0
                start = (i, j)
            elif graph[i][j] == "*":
                visited[i][j] = -999
                q.append((i, j))

    q.append(start)
    print(bfs())