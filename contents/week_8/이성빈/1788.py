# 백준 1788번 피보나치 수의 확장
# SILVER 3
# 알고리즘 분류 : 수학, 다이나믹 프로그래밍
N = int(input())
dp = [0,1]
for i in range(2,abs(N)+1) :
    dp.append((dp[i-2] + dp[i-1])%1000000000)
if N > 0 :
    print(1)
    print(dp[-1])
elif N < 0 :
    if N%2 :
        print(1)
    else :
        print(-1)
    print(dp[-1])
else :
    print(0)
    print(0)