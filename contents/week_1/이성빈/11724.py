# 백준 11724번 연결 요소의 개수
# SILVER 2
# 알고리즘 분류 : 그래프 이론, 그래프 탐색, 너비 우선 탐색, 깊이 우선 탐색
# DFS로 탐색하면서 한 연결요소에서 갈 수 있는 모든 경우를 탐색하고 cnt를 1증가시킴
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
def dfs(v) :
    check[v] = 1
    for i in g[v] :
        if not check[i] :
            dfs(i)
N,M = map(int,input().split())
g = [[] for _ in range(N+1)]
check = [0]*(N+1)
cnt = 0
for _ in range(M) :
    u,v = map(int,input().split())
    g[u].append(v)
    g[v].append(u)
for i in range(1,N+1) :
    if check[i] == 0 :
        dfs(i)
        cnt += 1
print(cnt)