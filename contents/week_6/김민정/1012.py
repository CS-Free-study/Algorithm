# 1012 유기농 배추
# 실버 2


import sys
from collections import deque

sys.setrecursionlimit(100000)

def bfs(i,j):
    visited[i][j] = 1
    que.append((i,j))

    while len(que) > 0:
        v = que.popleft()

        i = v[0]
        j = v[1]
        if i > 0 and (graph[i - 1][j] == 1 and visited[i - 1][j] == 0):
            que.append((i-1,j)) # 하(밑)으로 가는 경우
            visited[i-1][j] = 1
        if j > 0 and (graph[i][j - 1] == 1 and visited[i][j - 1] == 0):
            que.append((i,j-1))
            visited[i][j-1] = 1
        if i < n-1 and (graph[i + 1][j] == 1 and visited[i + 1][j] == 0):
            que.append((i+1,j))
            visited[i+1][j] = 1
        if j < m-1 and (graph[i][j + 1] == 1 and visited[i][j + 1] == 0):
            que.append((i,j+1))
            visited[i][j+1] = 1



input = sys.stdin.readline
t = int(input())


for _ in range(t):
    m, n, k = map(int, input().split())
    graph = [[0]*m for _ in range(n)]
    visited = [[0]*m for _ in range(n)]
    que = deque([])
    for _ in range(k):
        a, b = map(int, input().split())
        graph[b][a] = 1
    cnt = 0
    for i in range(0,n):
        for j in range(0,m):
            if graph[i][j] == 1 and visited[i][j] == 0:
                cnt += 1
                bfs(i, j)
    print(cnt)


