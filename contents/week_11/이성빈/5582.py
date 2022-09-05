# 백준 5582번 공통 부분 문자열
# GOLD 5
# 알고리즘 분류 : 다이나믹 프로그래밍, 문자열
A = input()
B = input()
dp = [[0]*(len(A)+1) for _ in range(len(B)+1)]
ans = 0
for i in range(len(B)) :
    for j in range(len(A)) :
        if A[j] == B[i] :
            dp[i+1][j+1] = dp[i][j] + 1
            ans = max(ans,dp[i+1][j+1])
        else :
            dp[i+1][j+1] = 0
print(ans)