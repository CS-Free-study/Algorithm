# 백준 25375번 아주 간단한 문제
# SILVER 5
# 알고리즘 분류 : 수학, 정수론
import math
import sys
input = sys.stdin.readline
Q = int(input())
for _ in range(Q) :
    a,b = map(int,input().split())
    check = 1
    for i in range(0,b,a) :
        if i == 0 :
            continue
        if math.gcd(i,b-i) == a :
            print(1)
            check = 0
            break
    if check :
        print(0)

# 다른풀이
import sys
input = sys.stdin.readline
Q = int(input())
for _ in range(Q) :
    a,b = map(int,input().split())
    if b%a == 0 and b//a != 1:
        print(1)
    else :
        print(0)