# 백준 1145번 적어도 대부분의 배수
# BRONZE 1
# 알고리즘 분류 : 브루트포스 알고리즘

li = list(map(int,input().split()))
i = 1
while True :
    cnt = 0
    for j in range(5) :
        if i%li[j] == 0 :
            cnt += 1
    if cnt >= 3 :
        print(i)
        break
    i += 1

# 다른풀이
import sys
li = list(map(int,input().split()))

ans = sys.maxsize

def gcd(a,b) :
    if a < b :
        a,b = b,a
    while a%b :
        a,b = b, a%b
    return b

def lcm(a,b) :
    return a*b//gcd(a,b)
for i in li :
    for j in li :
        for k in li :
            if i != j and i != k and j != k :
                ans = min(lcm(lcm(i,j),k),ans)
print(ans)