import sys
input = sys.stdin.readline

n = int(input())
a = int(input())
b = [int(input()) for _ in range(n - 1)]
ans = 0

if n == 1:
    print(0)
else:
    b.sort(reverse = True)

    while b[0] >= a:
        b[0] -= 1
        a += 1
        ans += 1
        b.sort(reverse = True)
    
    print(ans)