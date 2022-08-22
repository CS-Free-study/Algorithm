# 백준 10971번 외판원 순회2
# SILVER 2
# 알고리즘 분류 : 브루트포스 알고리즘, 백트래킹, 외판원 순회 문제
# 이해 하기 힘든 문제
import sys
N = int(input())
li = [list(map(int,input().split())) for _ in range(N)]
ans = sys.maxsize
check = [0]*N
def dfs(v,x,a) :
    global ans

    if x == N :
        if li[v][0] :
            ans = min(ans,a+li[v][0])
        return
    for i in range(N) :
        if li[v][i] and not check[i] :
            check[i] = 1
            dfs(i,x+1,a+li[v][i])
            check[i] = 0
for i in range(N) :
    check[i] = 1
    dfs(i,1,0)
print(ans)