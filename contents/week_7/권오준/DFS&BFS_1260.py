# 백준 1260, DFS와 BFS, 실버2
import sys
from collections import deque
input = sys.stdin.readline

def dfs(graph, v, visited, ans):
    visited[v] = True

    graph[v].sort()
    for i in graph[v]:
        if not visited[i]:
            ans.append(i)
            dfs(graph, i, visited, ans)

def bfs(graph, v, visited, ans):
    q = deque([v])
    visited[v] = True
    
    while q:
        node = q.popleft()
        ans.append(node)
        
        graph[node].sort()
        for i in graph[node]:
            if not visited[i]:
                q.append(i)
                visited[i] = True

n, m, v = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visitedDFS = [False] * (n + 1)
visitedBFS = [False] * (n + 1)
ansDFS = [v]
ansBFS = []

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

dfs(graph, v, visitedDFS, ansDFS)
bfs(graph, v, visitedBFS, ansBFS)

print(" ".join(map(str, ansDFS)))
print(" ".join(map(str, ansBFS)))

