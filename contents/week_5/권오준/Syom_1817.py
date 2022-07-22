# 백준 1817, 짐 챙기는 숌, 실버5
import sys
input = sys.stdin.readline

n, box = map(int, input().split())
if n == 0:
    print(0)
else:
    books = list(map(int, input().split()))

    weight = 0
    ans = 1

    for i in books:
        weight += i
        if weight > box:
            ans += 1
            weight = i
        
    print(ans)
