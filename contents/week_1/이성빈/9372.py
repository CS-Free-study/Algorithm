# 백준 9372번 상근이의 여행
# SILVER 4
# 알고리즘 분류 : 그래프 이론, 트리
# DFS로 순회하는 횟수를 세서 출력
# 모든 그래프가 연결되어 있기 때문에 N-1을 출력해도 된다
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
T = int(input())
def dfs(v) :
    global cnt
    cnt += 1
    check[v] = 1
    for i in g[v] :
        if not check[i] :
            dfs(i)
for _ in range(T) :
    cnt = 0
    N,M = map(int,input().split())
    g = [[] for _ in range(N+1)]
    check = [0]*(N+1)
    for i in range(M) :
        a,b = map(int,input().split())
        g[a].append(b)
        g[b].append(a)
    dfs(1)
    print(cnt-1)

# 다른 풀이
import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T) :
    N,M= map(int,input().split())
    for i in range(M) :
        input()
    print(N-1)