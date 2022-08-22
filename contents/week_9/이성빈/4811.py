# 백준 4811번 알약
# GOLD 5
# 알고리즘 분류 : 다이나믹 프로그래밍
# 카탈란 수를 구하는 문제라는 것을 풀고 난 뒤 검색으로 알게 됨.
# 카탈란 수 : 1,25,14,42,132 ....
# https://blog.naver.com/apple8718/222741860515 카탈란 수 관련 정리

# 내 풀이
import sys
dp = [0]*31
dp[1] = 1
before = [0]*31
before[1] = 1 
after = [0]*32

for i in range(2,31) :
    for j in range(i,0,-1) :
        for k in range(1,j+2) :
            after[k] += before[j]
    dp[i] = sum(after)
    before = after.copy()
    after = [0]*32
while 1 :
    N = int(sys.stdin.readline())
    if N == 0 :
        break
    print(dp[N])

# 다른 풀이
from math import factorial
import sys
while 1 :
    N = int(sys.stdin.readline())
    if N == 0 :
        break
    print((factorial(2*N))//factorial(N)//factorial(N+1))

# 다른 풀이
import sys
dp = [[0]*31 for _ in range(31)]
for i in range(31) :
    for j in range(i,31) :
        if i == 0 :
            dp[i][j] = 1
        else :
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
while 1 :
    N = int(sys.stdin.readline())
    if N == 0 :
        break
    print(dp[N][N])