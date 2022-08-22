# 백준 2667, 단지번호붙이기, 실버1
import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
graph = []
visited = [[0] * n for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
ans = []

for _ in range(n):
    graph.append(list(map(int, input().rstrip())))

def bfs(x, y):
    cnt = 1
    q = deque()
    q.append((x, y))
    visited[x][y] = 1

    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1 and visited[nx][ny] == 0:
                q.append((nx, ny))
                visited[nx][ny] = 1
                cnt += 1

    ans.append(cnt)

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1 and visited[i][j] == 0:
            bfs(i, j)

ans.sort()
print(len(ans))
print('\n'.join(map(str, ans)))