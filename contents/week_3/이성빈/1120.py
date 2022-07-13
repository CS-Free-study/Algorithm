# 백준 1120번 문자열
# SILVER 4
# 알고리즘 분류 : 문자열, 브루트포스 알고리즘
A,B = map(str,input().split())
gap = len(B) - len(A)
ans = 50
for i in range(gap+1) :
    cnt = 0
    for j in range(len(A)) :
        if A[j] != B[j+i] :
            cnt += 1
    ans = min(ans,cnt)
print(ans)