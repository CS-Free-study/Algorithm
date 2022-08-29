import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().rstrip())) for _ in range(n)]
q = deque()
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    q.append((0, 0))

    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y

            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                q.append((nx, ny))

    return graph[-1][-1]

print(bfs())