# 백준 9465번 스티커
# SILVER 1
# 알고리즘 분류 : 다이나믹 프로그래밍
# 2줄을 갖고 DP비교를 하면서 최적의 값을 찾는 문제
import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T) :
    N = int(input())
    li1 = list(map(int,input().split()))
    li2 = list(map(int,input().split()))
    dp1 = [0]*N
    dp2 = [0]*N
    dp1[0] = li1[0]
    dp2[0] = li2[0]
    if N == 1 :
        print(max(dp1[0],dp2[0]))
        continue
    dp1[1] = dp2[0] + li1[1]
    dp2[1] = dp1[0] + li2[1]
    for i in range(2,N) :
        dp1[i] = max(dp2[i-2]+li1[i],dp2[i-1]+li1[i])
        dp2[i] = max(dp1[i-2]+li2[i],dp1[i-1]+li2[i])
    print(max(dp1[-1],dp2[-1]))