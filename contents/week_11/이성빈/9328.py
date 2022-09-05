# 백준 9328번 열쇠
# GOLD 1
# 알고리즘 분류 : 구현, 그래프 이론, 그래프 탐색, 너비 우선 탐색
# 처리해줘야 될게 너무 많았던 문제
import sys
from collections import deque
input = sys.stdin.readline
dx = [1,-1,0,0]
dy = [0,0,1,-1]
k = []
def insert(x,y) :
    global ans
    num = ord(li[y][x])
    if li[y][x] == '*' :
        return
    if check[y][x] :
        return
    if num == 46 :
        q.append([x,y])
    elif num == 36 :
        ans += 1
        q.append([x,y])
    elif 64 < num < 91 :
        if key[num-65] :
            q.append([x,y])
        else :
            door[num-65].append([x,y])
    elif 96 < num < 123 :
        if not key[num-97] :
            key[num-97] = 1
            for i in door[num-97] :
                q.append(i)
        q.append([x,y])
    check[y][x] = 1

def bfs() :
    global ans
    while q :
        x,y = q.popleft()
        for i in range(4) :
            x_ = x + dx[i]
            y_ = y + dy[i]
            if x_ < 0 or x_ > w-1 or y_ < 0 or y_ > h-1 :
                continue
            insert(x_,y_)

T = int(input())
for _ in range(T) :
    h,w = map(int,input().split())
    li = [list(input().rstrip()) for _ in range(h)]
    val = input().rstrip()
    q = deque()
    ans = 0
    key = [0]*26
    door = [[] for _ in range(26)]
    check = [[0]*w for _ in range(h)]
    q = deque()
    if val != '0' :
        for i in val :
            key[ord(i)-97] = 1
    for i in range(h) :
        insert(0,i)
        insert(w-1,i)
    for i in range(w) :
        insert(i,0)
        insert(i,h-1)
    bfs()
    print(ans)