# 백준 1173 운동
# BRONZE 2
# 알고리즘 분류 : 구현, 시뮬레이션
# 운동을 할 수 없느 경우를 생각 못했음.
N,m,M,T,R = map(int,input().split())
cnt = 0
b = m
if m > M or m+T > M :
    print(-1)
    exit()
while N :
    if b+T <= M :
        b += T
        cnt += 1
        N -= 1
    else :
        b -= R
        if b < m :
            b = m
        cnt += 1
print(cnt)