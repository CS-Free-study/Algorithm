# 백준 1325번 효율적인 해킹
# SILVER 1
# 알고리즘 분류 : 그래프 이론, 그래프 탐색, 너비 우선 탐색, 깊이 우선 탐색
# Python3 시간 초과 Pypy 3 제출
# dfs 시간초과 발생
import sys
sys.setrecursionlimit(10**4)
input = sys.stdin.readline
N,M = map(int,input().split())
g = [[0] for _ in range(N+1)]
ans = []
max_val = 0
def dfs(v) :
    global cnt
    cnt += 1
    check[v] = 1
    for i in g[v] :
        if not check[i] :
            dfs(i)
for _ in range(M) :
    A,B = map(int,input().split())
    g[B].append(A)
for i in range(1,N+1) :
    cnt = 0
    check = [0]*(N+1)
    dfs(i)
    if cnt > max_val :  
        max_val = cnt
        ans = []
        ans.append(i)
    elif cnt == max_val :
        ans.append(i)
print(*ans)

# bfs AC
import sys
from collections import deque
input = sys.stdin.readline
N,M = map(int,input().split())
g = [[0] for _ in range(N+1)]
ans = []
max_val = 0
def bfs(v) :
    q = deque()
    q.append(v)
    check[v] = 1
    cnt = 1
    while q :
        v = q.popleft()
        for i in g[v] :
            if check[i] == 0 :
                check[i] = 1
                cnt += 1
                q.append(i)
    return cnt

for _ in range(M) :
    A,B = map(int,input().split())
    g[B].append(A)
for i in range(1,N+1) :
    check = [0]*(N+1)
    cnt = bfs(i)
    if cnt > max_val :  
        max_val = cnt
        ans = []
        ans.append(i)
    elif cnt == max_val :
        ans.append(i)
print(*ans)