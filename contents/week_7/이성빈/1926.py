# 백준 1926번 그림
# SILVER 1
# 알고리즘 분류 : 그래프 이론, 그래프 탐색, 너비 우선 탐색, 깊이 우선 탐색
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
N,M = map(int,input().split())
li = [list(map(int,input().split())) for _ in range(N)]
ans = []
def dfs(x,y) :
    global cnt
    if x < 0 or x > M-1 or y < 0 or y > N-1 :
        return False
    if li[y][x] == 1 :
        cnt += 1
        li[y][x] = 2
        dfs(x+1,y)
        dfs(x-1,y)
        dfs(x,y+1)
        dfs(x,y-1)
        return True
    return False
for i in range(N) :
    for j in range(M) :
        cnt = 0
        if dfs(j,i) :
            ans.append(cnt)
print(len(ans))
if ans :
    print(max(ans))
else :
    print(0)