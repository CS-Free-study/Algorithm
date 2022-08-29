import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = list(map(int, input().split()))
ans = 0

def bt(idx, res):
    global ans

    if idx == n:
        return

    res += a[idx]
    
    if res == m:
        ans += 1

    bt(idx + 1, res)
    bt(idx + 1, res - a[idx])

bt(0, 0)
print(ans)