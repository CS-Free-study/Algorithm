# 백준 16928번 뱀과 사다리 게임
# GOLD 5
# 알고리즘 분류 : 그래프 이론, 그래프 탐색, 너비 우선 탐색
# BFS로 탐색하면서 이동횟수를 그래프에 저장
import sys
from collections import deque
input = sys.stdin.readline
move =[1,2,3,4,5,6]
N,M = map(int,input().split())
q = deque()
g = [0]*101
li = [0]*101
def bfs(v):
    q.append(v)
    while q :
        v = q.popleft()
        for i in range(6) :
            v_ = v + move[i]
            if v_ > 100 :
                continue
            if g[v_] :
                v_ = g[v_]
            if li[v_] == 0 :
                li[v_] = li[v] + 1
                q.append(v_)
for i in range(N) :
    x,y = map(int,input().split())
    g[x] = y
for i in range(M) :
    x,y = map(int,input().split())
    g[x] = y
bfs(1)
print(li[-1])