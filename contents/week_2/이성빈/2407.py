# 백준 2407번 조합
# SILVER 4
# 알고리즘 분류 : 수학, 다이나믹 프로그래밍, 조합론, 임의 정밀도/ 큰 수 연산
# nC1 부터 계산해서 dp에 넣어주어 nCm 까지 계산한다
# math 라이브러리를 통해 손 쉽게 계산할 수 있음.
n,m = map(int,input().split())
m = min(n-m,m)
dp = [0]*m
dp[0] = n
for i in range(1,m) :
    dp[i] = dp[i-1]*(n-i)//(i+1)
print(dp[-1])

# 다른풀이
import math
n,m = map(int,input().split())
print(math.comb(n,m))