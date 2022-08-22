# 백준 11558번 The Game of Death
# SILVER 4
# 알고리즘 분류 : 구현, 그래프 이론, 그래프 탐색, 시뮬레이션
import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T) :
    N = int(input())
    li = [0] + [int(input()) for i in range(N)]
    check = [0]*(N+1)
    cnt = 0
    ans = 0
    a = 1
    while not check[a] :
        check[a] = 1
        if a == N :
            ans = cnt
            break
        a = li[a]
        cnt += 1
    print(ans)