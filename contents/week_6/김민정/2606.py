# 2606 바이러스
# 실버 3

import sys
sys.setrecursionlimit(1000000)
def dfs(v):
    visited[v] = 1

    for x in graph[v]:
        if visited[x] == 0:
            dfs(x)

input = sys.stdin.readline

n = int(input())
k = int(input())

graph = [[] for _ in range(n)]
visited = [0 for _ in range(n)]


for _ in range(k):
    a, b = map(int, input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)

dfs(0)
print(visited.count(1)-1)





