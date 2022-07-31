# 백준 9205번 맥주 마시면서 걸어가기
# SILVER 1
# 알고리즘 분류 : 그래프 이론, 그래프 탐색, 너비 우선 탐색
from collections import deque
def bfs(x,y) :
    q = deque()
    q.append([x,y])

    while q :
        x,y = q.popleft()
        if abs(x-a_x) + abs(y-a_y) <= 1000 :
            return True
        for i in range(N) :
            x_ = li[i][0]
            y_ = li[i][1]
            if abs(x-x_) + abs(y-y_) <= 1000 and not check[i] :
                check[i] = 1
                q.append([x_,y_])
    return False
T = int(input())
for _ in range(T) :
    N = int(input())
    h_x,h_y = map(int,input().split())
    li = [list(map(int,input().split())) for i in range(N)]
    a_x,a_y = map(int,input().split())
    check = [0]*(N+1)
    if bfs(h_x,h_y) :
        print("happy")
    else :
        print("sad")