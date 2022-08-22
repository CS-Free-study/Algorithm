# 백준 1389번 케빈 베이컨의 6단계 법칙
# SILVER 1
# 알고리즘 분류 : 그래프 이론, 그래프 탐색, 너비 우선 탐색, 플로이드-워셜
# BFS 풀이
import sys
from collections import deque
input = sys.stdin.readline
N,M = map(int,input().split())
g = [[0]*(N+1) for _ in range(N+1)]
ans = [0]*(N+1)
ans[0] = sys.maxsize
def bfs(v) :
    cnt = 0
    q = deque()
    q.append(v)
    check[v] = 1
    while q :
        v = q.popleft()
        for i in range(1,N+1) :
            if check[i] == 0 and g[v][i] == 1 :
                q.append(i)
                check[i] = check[v] + 1
    return sum(check)
for _ in range(M) :
    a,b = map(int,input().split())
    g[a][b] = 1
    g[b][a] = 1
for i in range(1,N+1) :
    check = [0]*(N+1)
    ans[i] = bfs(i)
print(ans.index(min(ans)))


# 플로이드-워셜 풀이
import sys
input = sys.stdin.readline
INF = sys.maxsize
N,M = map(int,input().split())
cnt = [[INF]*(N+1) for _ in range(N+1)]
for i in range(M) :
    a,b = map(int,input().split())
    cnt[a][b] = 1
    cnt[b][a] = 1
for i in range(N+1) :
    cnt[i][i] = 0
for k in range(N+1) :
    for i in range(N+1) :
        for j in range(N+1) :
            cnt[i][j] = min(cnt[i][j], cnt[i][k] + cnt[k][j])
ans = [sum(cnt[i][1:]) for i in range(1,N+1)]
print(ans.index(min(ans)) + 1)