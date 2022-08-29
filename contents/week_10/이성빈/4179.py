# 백준 4179번 불!
# GOLD 4
# 알고리즘 분류 : 그래프 이론, 그래프 탐색, 너비 우선 탐색
from collections import deque
import sys
input = sys.stdin.readline
q = deque()
dx = [0,0,1,-1]
dy = [1,-1,0,0]
def bfs() :
    while q :
        x,y,c = q.popleft()
        if c and (x == 0 or x == C-1 or y == 0 or y == R-1) :
            return check[y][x] + 1
        for i in range(4) :
            x_ = x + dx[i]
            y_ = y + dy[i]
            if x_ < 0 or x_ > C-1 or y_ < 0 or y_ > R-1 :
                continue
            if c :
                if li[y_][x_] == '.' and not check[y_][x_] :
                    check[y_][x_] = check[y][x] + 1
                    q.append([x_,y_,1])
            else :
                if li[y_][x_] == '.' or li[y_][x_] == 'J' :
                    li[y_][x_] = 'F'
                    q.append([x_,y_,0])
    return 'IMPOSSIBLE'
R,C = map(int,input().split())
li = [list(input()) for _ in range(R)]
check = [[0]*C for _ in range(R)]
for i in range(R) :
    for j in range(C) :
        if li[i][j] == 'J' :
            a,b = j,i
        if li[i][j] == 'F' :
            q.append([j,i,0])
q.append([a,b,1])
print(bfs())