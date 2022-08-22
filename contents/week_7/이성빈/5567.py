# 백준 5567번 결혼식
# SILVER 2
# 알고리즘 분류 : 그래프 이론, 그래프 탐색
import sys
N = int(input())
M = int(input())
g = [[] for _ in range(N+1)]
cnt = 0
check = [0]*(N+1)
check[1] = 1
for _ in range(M) :
    a,b = map(int,input().split())
    g[a].append(b)
    g[b].append(a)
for i in g[1] :
    if check[i] == 0 :
        cnt += 1
        check[i] = 1
    for j in g[i] :
        if check[j] == 0 :
            cnt += 1
            check[j] = 1
print(cnt)