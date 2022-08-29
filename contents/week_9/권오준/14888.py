import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
pl, mi, mu, di = list(map(int, input().split()))
maxVal = -1e9
minVal = 1e9

def dfs(idx, total, pl, mi, mu, di):
    global maxVal, minVal

    if idx == n:
        maxVal = max(maxVal, total)
        minVal = min(minVal, total)
        return
    
    if pl:
        dfs(idx + 1, total + a[idx], pl - 1, mi, mu, di)
    if mi:
        dfs(idx + 1, total - a[idx], pl, mi - 1, mu, di)
    if mu:
        dfs(idx + 1, total * a[idx], pl, mi, mu - 1, di)
    if di:
        dfs(idx + 1, int(total / a[idx]), pl, mi, mu, di - 1)

dfs(1, a[0], pl, mi, mu, di)
print(maxVal)
print(minVal)
        