import sys
input = sys.stdin.readline

n = int(input())
cnt = 0

for _ in range(n):
    s = input().rstrip()
    a = []

    for i in s:
        if i not in a:
            a.append(i)
        else:
            if i != a[-1]:
                cnt += 1
                break
    
print(n - cnt)