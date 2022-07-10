# 백준 4963번 섬의 개수
# SILVER 2
# 알고리즘 분류 : 그래프
import sys
from collections import deque
input = sys.stdin.readline
dx = [1,-1,0,0,1,-1,1,-1]
dy = [0,0,1,-1,1,-1,-1,1]
def bfs(x,y) :
    q = deque()
    check = [[0]*a for _ in range(b)]
    q.append([x,y])
    while q:
        x,y = q.popleft()
        for i in range(8) :
            x_ = x + dx[i]
            y_ = y + dy[i]
            if x_ < 0 or x_ > a-1 or y_ < 0 or y_ > b-1 :
                continue
            if li[y_][x_] == 1 and not check[y_][x_] :
                li[y_][x_] = 0
                check[y_][x_] = 1
                q.append([x_,y_])


while True :
    a,b = map(int,input().split())
    cnt = 0
    if a+b == 0 :
        break
    li = [list(map(int,input().split())) for _ in range(b)]
    for i in range(a) :
        for j in range(b) :
            if li[j][i] == 1 :
                bfs(i,j)
                cnt += 1
    print(cnt)