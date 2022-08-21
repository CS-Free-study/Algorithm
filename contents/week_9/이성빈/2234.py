# 백준 2234번 성곽
# GOLD 3
# 알고리즘 분류 : 그래프 이론, 그래프 탐색, 너비 우선 탐색, 비트마스킹
# 첫 풀이
import sys
from collections import deque
input = sys.stdin.readline
dx = [0,1,0,-1]
dy = [1,0,-1,0]
N,M = map(int,input().split())
li = [list(map(int,input().split())) for _ in range(M)]
ans_1 = 0
ans_2 = 0
ans_3 = 0
def bfs(x,y) :
    cnt = 1
    q = deque()
    q.append([x,y])
    check[y][x] = 1
    while q :
        x,y = q.popleft()
        val = list(map(int,bin(li[y][x])[2:]))
        val = [0]*(4-len(val)) + val
        for i in range(4) :
            if val[i] == 0 :
                x_ = x + dx[i]
                y_ = y + dy[i]
                if x_ < 0 or x_ > N-1 or y_ < 0 or y_ > M-1 :
                    continue
                if not check[y_][x_] :
                    q.append([x_,y_])
                    check[y_][x_] = 1
                    cnt += 1
    return cnt

check = [[0]*N for _ in range(M)]
for i in range(N) :
    for j in range(M) :
        if not check[j][i] :
            ans_1 += 1
            ans_2 = max(bfs(i,j),ans_2)
for i in range(N) :
    for j in range(M) :
        for m in range(4) :
            check = [[0]*N for _ in range(M)]
            res = list(map(int,bin(li[j][i])[2:]))
            res = [0]*(4-len(res)) + res
            if res[m] :
                res[m] = 0
                li[j][i] = res[0]*8 + res[1]*4 + res[2]*2 + res[3]*1
                ans_3 = max(bfs(i,j),ans_3)
                res[m] = 1
                li[j][i] = res[0]*8 + res[1]*4 + res[2]*2 + res[3]*1
print(ans_1)
print(ans_2)
print(max(ans_3,ans_2))

# 개선된 풀이
import sys
from collections import deque
input = sys.stdin.readline
dx = [0,1,0,-1]
dy = [1,0,-1,0]
N,M = map(int,input().split())
li = [list(map(int,input().split())) for _ in range(M)]
barrier = deque()
ans_1 = 0
ans_2  = [0]
ans_3 = 0
def bfs(x,y) :
    cnt = 1
    q = deque()
    q.append([x,y])
    check[y][x] = ans_1
    while q :
        x,y = q.popleft()
        val = list(map(int,bin(li[y][x])[2:]))
        val = [0]*(4-len(val)) + val
        for i in range(4) :
            x_ = x + dx[i]
            y_ = y + dy[i]
            if val[i] == 0 :
                if x_ < 0 or x_ > N-1 or y_ < 0 or y_ > M-1 :
                    continue
                if not check[y_][x_] :
                    q.append([x_,y_])
                    check[y_][x_] = ans_1
                    cnt += 1
            else :
                if x_ < 0 or x_ > N-1 or y_ < 0 or y_ > M-1 :
                    continue
                if not check[y_][x_] :
                    barrier.append([x,y,x_,y_])
    return cnt

check = [[0]*N for _ in range(M)]
for i in range(N) :
    for j in range(M) :
        if not check[j][i] :
            ans_1 += 1
            ans_2.append(bfs(i,j))
while barrier :
    x,y,x_,y_ = barrier.popleft()
    a,b = check[y][x],check[y_][x_]
    if a != b :
        ans_3 = max(ans_3,ans_2[a]+ans_2[b])
print(ans_1)
print(max(ans_2))
print(ans_3)