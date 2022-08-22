# 백준 1986번 체스
# SILVER 2
# 알고리즘 분류 : 구현
# 구현 어렵다
N,M = map(int,input().split())
check = [[0]*M for _ in range(N)]
Q = list(map(int,input().split()))
K = list(map(int,input().split()))
P = list(map(int,input().split()))

def place(A) :
    for i in range(1,A[0]*2,2) :
        check[A[i]-1][A[i+1]-1] = 2

def locate(x,y) :
    if x < 0 or x > M-1 or y < 0 or y > N-1 :
        return
    check[y][x] = 1

place(Q)
place(K)
place(P)

for i in range(1,Q[0]*2,2) :
    y,x = Q[i]-1, Q[i+1]-1
    for j in range(x-1,-1,-1) :
        if check[y][j] == 2 :
            break
        check[y][j] = 1
    for j in range(x+1,M) :
        if check[y][j] == 2 :
            break
        check[y][j] = 1
    for j in range(y-1,-1,-1) :
        if check[j][x] == 2 :
            break
        check[j][x] = 1
    for j in range(y+1,N) :
        if check[j][x] == 2 :
            break
        check[j][x] = 1

    x_ = x - 1
    y_ = y - 1
    while x_ >= 0 and y_ >= 0 :
        if check[y_][x_] == 2 :
            break
        check[y_][x_] = 1
        x_ -= 1
        y_ -= 1

    x_ = x - 1
    y_ = y + 1
    while x_ >= 0 and y_ < N :
        if check[y_][x_] == 2 :
            break
        check[y_][x_] = 1
        x_ -= 1
        y_ += 1

    x_ = x + 1
    y_ = y - 1
    while x_ < M and y_ >= 0 :
        if check[y_][x_] == 2 :
            break
        check[y_][x_] = 1
        x_ += 1
        y_ -= 1

    x_ = x + 1
    y_ = y + 1
    while x_ < M and y_ < N :
        if check[y_][x_] == 2 :
            break
        check[y_][x_] = 1
        x_ += 1
        y_ += 1

for i in range(1,K[0]*2,2) :
    y,x = K[i]-1, K[i+1]-1
    locate(x+1,y+2)
    locate(x+2,y+1)
    locate(x-1,y+2)
    locate(x-2,y+1)
    locate(x-1,y-2)
    locate(x-2,y-1)
    locate(x+1,y-2)
    locate(x+2,y-1)
ans = 0
for i in check :
    ans += i.count(0)
print(ans)