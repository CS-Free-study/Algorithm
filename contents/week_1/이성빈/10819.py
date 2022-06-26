# 백준 10819번 차이를 최대로
# SILVER 2
# 알고리즘 분류 : 브루트포스 알고리즘, 백트래킹
# 다음순열을 구하고 그 순열에서 값을 구하고 최대값이랑 비교하며 업데이트 해나감
N = int(input())
A = sorted(list(map(int,input().split())))
def next(A) :
    k = -1
    for i in range(N-1,0,-1) :
        if A[i-1] < A[i] :
            k = i-1
            break
    if k == -1 :
        return 0
    for i in range(N-1,0,-1) :
        if A[k] < A[i] :
            A[k],A[i] = A[i],A[k]
            A = A[:k+1] + sorted(A[k+1:])
            return A
val = 0
while True :
    s = 0
    for i in range(N-1) :
        s += abs(A[i+1]-A[i])
    val = max(val,s)
    A = next(A)
    if A == 0 :
        break
print(val)