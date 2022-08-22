# 백준 2660번 회장뽑기
# GOLD 5
# 알고리즘 분류 : 그래프 이론, 그래프 탐색, 너비 우선 탐색, 플로이드-워셜

# 플로이드-워셜 풀이
import sys
input = sys.stdin.readline
INF = sys.maxsize

N = int(input())
g = [[INF]*(N+1) for _ in range(N+1)]
while True :
    a,b = map(int,input().split())
    if a == -1 and b == -1 :
        break
    g[a][b] = 1
    g[b][a] = 1
for i in range(N+1) :
    g[i][i] = 0

for k in range(N+1) :
    for i in range(N+1) :
        for j in range(N+1) :
            g[i][j] = min(g[i][j],g[i][k]+g[k][j])
ans = [max(g[i][1:]) for i in range(1,N+1)]
min_val = min(ans)
print(min_val, ans.count(min_val))
for i in range(N) :
    if ans[i] == min_val :
        print(i+1 ,end= ' ')


# bfs 풀이
import sys
from collections import deque
input = sys.stdin.readline
N = int(input())
g = [[0] for _ in range(N+1)]
ans = [0]*N
while True :
    a,b = map(int,input().split())
    if a == -1 and b == -1 :
        break
    g[a].append(b)
    g[b].append(a)

def bfs(v) :
    q = deque()
    q.append([v,0])
    check[v] = 1
    while q :
        v,m = q.popleft()
        for i in g[v] :
            if not check[i] :
                check[i] = 1
                q.append([i,m+1])
    return m


for i in range(1,N+1) :
    check = [0]*(N+1)
    ans[i-1] = bfs(i)
min_val = min(ans)
print(min_val,ans.count(min_val))
for i in range(N) :
    if ans[i] == min_val :
        print(i+1,end = ' ')