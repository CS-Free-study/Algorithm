import sys
input = sys.stdin.readline

n, m = map(int, input().split())
stk = [[0] for _ in range(7)]
ans = 0

for _ in range(n):
    a, b = map(int, input().split())

    while stk[a][-1] > b:
        stk[a].pop()
        ans += 1

    if stk[a][-1] == b:
        continue
    
    stk[a].append(b)
    ans += 1

print(ans)