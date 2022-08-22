# 백준 1817번 짐 챙기는 숌
# SILVER 5
# 알고리즘 분류 : 구현, 그리디 알고리즘
N,M = map(int,input().split())
if N == 0 :
    print(0)
    exit()
li = list(map(int,input().split()))
cnt = 0
val = 0
for i in range(N) :
    if val + li[i] > M :
        cnt += 1
        val = li[i]
    elif val + li[i] == M :
        cnt += 1
        val = 0
    else :
        val += li[i]
if val != 0 :
    cnt += 1
print(cnt)