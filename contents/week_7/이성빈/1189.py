# 백준 1189번 컴백홈 
# SILVER 1
# 알고리즘 분류 : 브루트포스 알고리즘, 백트래킹
import sys
sys.setrecursionlimit(10**6)
R,C,K = map(int,input().split())
li = [list(input()) for _ in range(R)]
dx = [1,-1,0,0]
dy = [0,0,1,-1]
check = [[0]*C for _ in range(R)]
ans = 0
def dfs(x,y,cnt) :
    global ans
    if x == C-1 and y == 0 :
        if cnt == K :
            ans += 1
        return
    for i in range(4) :
        x_ = x + dx[i]
        y_ = y + dy[i]
        if x_ < 0 or x_ > C-1 or y_ < 0 or y_ > R-1 or li[y_][x_] == 'T'or check[y_][x_]:
            continue
        check[y_][x_] = 1
        dfs(x_,y_,cnt+1)
        check[y_][x_] = 0
check[R-1][0] = 1
dfs(0,R-1,1)
print(ans)