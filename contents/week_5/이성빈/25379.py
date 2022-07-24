# 백준 25379번 피하자
# SILVER 4
# 알고리즘 분류 : 그리디 알고리즘
N = int(input())
li = list(map(int,input().split()))
even = 0
odd = 0
ans = [0,0]
for i in range(N) :
    if li[i]%2 :
        odd += 1
        ans[0] += even
    else :
        even += 1
        ans[1] += odd
print(min(ans))