# 백준 1958번 LCS 3
# GOLD 3
# 알고리즘 분류 : 다이나믹 프로그래밍, 문자열
# LCS와 다른 점은 2차원에서 3차원으로 바뀜
A = input()
B = input()
C = input()
dp = [[[0]*(len(A)+1) for _ in range(len(B)+1)] for _ in range(len(C)+1)]
for i in range(len(A)) :
    for j in range(len(B)) :
        for k in range(len(C)) :
            if A[i] == B[j] and B[j] == C[k] :
                dp[k+1][j+1][i+1] = dp[k][j][i] + 1
            else :
                dp[k+1][j+1][i+1] = max(dp[k][j+1][i+1],dp[k+1][j+1][i],dp[k+1][j][i+1])
print(dp[-1][-1][-1])