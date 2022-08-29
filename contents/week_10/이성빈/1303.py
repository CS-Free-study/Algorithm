# 백준 1303번 전쟁 - 전투
# SILVER 1
# 알고리즘 분류 : 그래프 이론, 그래프 탐색, 너비 우선 탐색, 깊이 우선 탐색
N,M = map(int,input().split())
li = [list(input()) for _ in range(M)]
check = [[0]*N for _ in range(M)]
dx = [1,-1,0,0]
dy = [0,0,1,-1]
b_cnt = 0
w_cnt = 0
def dfs(x,y) :
    global cnt
    cnt += 1
    check[y][x] = 1
    for i in range(4) :
        x_ = x + dx[i]
        y_ = y + dy[i]
        if x_ < 0 or x_ > N-1 or y_ < 0 or y_ > M-1 :
            continue

        if li[y_][x_] == color and not check[y_][x_] :
            dfs(x_,y_)

for i in range(M) :
    for j in range(N) :
        if not check[i][j] :
            color = li[i][j]
            cnt = 0
            dfs(j,i)
            if color == 'W' :
                w_cnt += (cnt)**2
            else :
                b_cnt += (cnt)**2
print(w_cnt,b_cnt)