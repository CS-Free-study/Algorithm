# 백준 10451번 순열 사이클
# SILVER 3
# 알고리즘 분류 : 순열 사이클 분할
import sys
input = sys.stdin.readline
T = int(input())
def dfs(v) :
    check[v] = 1
    for i in g[v] :
        if not check[i] :
            dfs(i)
for _ in range(T) :
    N = int(input())
    li = [0] + list(map(int,input().split()))
    g = [[] for _ in range(N+1)]
    cnt = 0
    for i in range(1,N+1) :
        g[i].append(li[i])
    check = [0]*(N+1)
    for i in range(1,N+1) :
        if not check[i] :
            dfs(i)
            cnt += 1
    print(cnt)