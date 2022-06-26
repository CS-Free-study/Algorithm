# 백준 2468번 안전 영역
# SILVER 1
# 알고리즘 분류 : 그래프, 브루트포스 알고리즘
# 일정 높이에서 안전구역의 개수를 DFS로 탐색하고 모든 경우를 탐색한 뒤 최대값을 출력
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
N = int(input())
li = [list(map(int,input().split())) for _ in range(N)]
res = []
cnt = 0
def dfs(x,y,h) :
    if x < 0 or x > N-1 or y < 0 or y > N-1 :
        return 1
    if li[x][y] > h :
        li[x][y] = h
        dfs(x-1,y,h)
        dfs(x+1,y,h)
        dfs(x,y-1,h)
        dfs(x,y+1,h)
        return 1
    return 0
for h in range(max(max(li)),-1,-1) :
    cnt = 0
    for x in range(N) :
        for y in range(N) :
            if dfs(x,y,h) :
                cnt += 1
    res.append(cnt)
print(max(res))