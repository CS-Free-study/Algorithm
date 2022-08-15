# 백준 6064번 카잉 달력
# SILVER 1
# 알고리즘 분류 : 수학, 정수론 ,중국인의 나머지 정리
# x,y에 -1을 빼는게 중요
import sys
import math
input = sys.stdin.readline
T = int(input())
for _ in range(T) :
    M,N,x,y = map(int,input().split())
    x -= 1
    y -= 1
    lcm = math.lcm(M,N)
    check = 1
    for i in range(lcm//M+1) :
        if (M*i + x)%N == y :
            print(M*i+x + 1)
            check = 0
            break
    if check :
        print(-1)