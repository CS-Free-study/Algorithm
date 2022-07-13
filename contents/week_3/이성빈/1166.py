# 백준 1166번 선물
# SILVER 3
# 알고리즘 분류 : 이분 탐색
# 일반적인 이분 탐색과 다르게 for문으로 이분 탐색을 하는 문제
N,L,W,H = map(int,input().split())
size = L*W*H
low = 0
high = L*W*H
for i in range(10000) :
    mid = (low+high)/2
    val = (L//mid)*(W//mid)*(H//mid)
    if val < N :
        high = mid
    else :
        low = mid 
        ans = mid
print(ans)