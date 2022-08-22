# 백준 25344번 행성 정렬
# SILVER 4
# 알고리즘 분류 : 수학, 정수론, 유클리드 호제법
N = int(input())
li = list(map(int,input().split()))
def gcd(a,b) :
    while b > 0 :
        a,b = b,a%b
    return a
for i in range(N-3) :
    li[i+1] = li[i]*li[i+1] // gcd(li[i],li[i+1])
print(li[-1])

import math
N = int(input())
print(math.lcm(*list(map(int,input().split()))))