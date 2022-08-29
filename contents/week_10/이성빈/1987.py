# 백준 1987번 알파벳
# GOLD 4
# 알고리즘 분류 : 그래프 이론, 그래프 탐색, 깊이 우선 탐색, 백트래킹
# Python3 시간초과 Pypy3 6052ms AC
import sys
input = sys.stdin.readline
dx = [1,-1,0,0]
dy = [0,0,1,-1]
check = [0]*26
ans = 0

R,C = map(int,input().split())
li = [list(input()) for _ in range(R)]

def dfs(x,y,val) :
    global ans
    ans = max(ans,val)
    for i in range(4) :
        x_ = x + dx[i]
        y_ = y + dy[i]
        if x_ < 0 or x_ > C-1 or y_ < 0 or y_ > R-1 :
            continue
        if check[ord(li[y_][x_])-65] :
            continue
        check[ord(li[y_][x_])-65] = 1
        dfs(x_,y_,val+1)
        check[ord(li[y_][x_])-65] = 0

check[ord(li[0][0])-65] = 1
dfs(0,0,1)
print(ans)