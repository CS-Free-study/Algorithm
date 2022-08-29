# 백준 16236번 아기 상어
# GOLD 3
# 알고리즘 분류 : 구현,그래프 이론, 그래프 탐색, 너비 우선 탐색, 시뮬레이션
# 어렵다
# 상어가 먹이를 발견하면 일단 배열에 저장하고 배열에서 가장 좋은 정답을 반환하고 다음 먹이를 탐색한다.
from collections import deque
dx = [0,0,-1,1]
dy = [-1,1,0,0]
baby_size = 2
ans = 0
cnt = 0

def bfs(x,y) :
    check = [[0]*N for _ in range(N)]
    q = deque()
    q.append([x,y,0])
    check[y][x] = 1
    eat = []
    while q :
        x,y,v = q.popleft()
        for i in range(4) :
            x_ = x + dx[i]
            y_ = y + dy[i]
            if x_ < 0 or x_ > N-1 or y_ < 0 or y_ > N-1 :
                continue
            if li[y_][x_] <= baby_size and not check[y_][x_] :
                check[y_][x_] = 1
                q.append([x_,y_,v+1])
            if 0 < li[y_][x_] < baby_size :
                eat.append([v+1,y_,x_])
    eat.sort()
    if eat :
        return eat[0]

N = int(input())
li = [list(map(int,input().split())) for _ in range(N)]
visit = [[0]*N for _ in range(N)]
for i in range(N) :
    for j in range(N) :
        if li[i][j] == 9 :
            li[i][j] = 0
            x,y = j,i
while True :
    val = bfs(x,y)
    if not val :
        break
    v,y,x = val
    li[y][x] = 0
    ans += v
    cnt += 1
    if cnt == baby_size :
        cnt = 0
        baby_size += 1
print(ans)