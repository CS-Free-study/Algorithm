#24479 알고리즘 수업 - 깊이 우선 탐색 1
#실버 2

import sys
sys.setrecursionlimit(10**9)

cnt = 1
def dfs(v):
    global cnt
    visited[v] = cnt
    graph[v].sort()

    for x in graph[v]:
        if visited[x] == 0:
            cnt += 1
            dfs(x)

n,m,v = map(int, sys.stdin.readline().split())
visited = [0 for _ in range(n)]
graph = [[] for _ in range(n)]

for _ in range(m):# 간선의 개수만큼 입력 받기
    a, b = map(int, sys.stdin.readline().split()) # 간선으로 연결되는 두 정점의 입력 받기
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)

dfs(v-1)

for i in range(0,n):
    print(visited[i])




