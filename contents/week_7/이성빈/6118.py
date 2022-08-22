# 백준 6118번 숨바꼭질
# SILVER 1
# 알고리즘 분류 : 그래프 이론, 그래프 탐색, 너비 우선 탐색
import sys
from collections import deque
input = sys.stdin.readline
N,M = map(int,input().split())
g = [[] for _ in range(N+1)]
check = [0]*(N+1)
def bfs(v) :
    q = deque()
    q.append(v)
    check[v] = 1
    while q :
        v = q.popleft()
        for i in g[v] :
            if not check[i] :
                q.append(i)
                check[i] = check[v] + 1
for _ in range(M) :
    a,b = map(int,input().split())
    g[a].append(b)
    g[b].append(a)
bfs(1)
val = max(check[1:])
idx = check.index(val)
print(idx,check[idx]-1,check.count(val))