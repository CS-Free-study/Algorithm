import sys
input = sys.stdin.readline

t = [(n * (n + 1) // 2) for n in range(1, 46)]
ans = [0] * 1001

for i in t:
    for j in t:
        for k in t:
            if i + j + k <= 1000:
                ans[i + j + k] = 1

for _ in range(int(input())):
    print(ans[int(input())])