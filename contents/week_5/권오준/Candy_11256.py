# 백준 11256, 사탕, 실버5
import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    candy, n = map(int, input().split())

    box = []
    ans = 0

    for _ in range(n):
        w, h = map(int, input().split())
        box.append(w * h)
    
    box.sort(reverse = True)

    for i in box:
        candy -= i
        ans += 1

        if candy <= 0:
            print(ans)
            break