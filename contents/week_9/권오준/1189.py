import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
ans = 0

def dfs(x, y, cnt):
    global ans
    visited[x][y] = True

    if [x, y] == [0, m - 1]:
        if cnt == k:
            ans += 1
            return
    
    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y

        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and graph[nx][ny] != 'T':
            visited[nx][ny] = True
            dfs(nx, ny, cnt + 1)
            visited[nx][ny] = False

dfs(n - 1, 0, 1)
print(ans)