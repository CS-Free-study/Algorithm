import sys
input = sys.stdin.readline

x, y, p1, p2 = map(int, input().split())
px = [p1]
py = [p2]
ans = -1

for i in range(1000):
    px.append(px[i] + x)
    py.append(py[i] + y)

    if px[-1] in py or py[-1] in px:
        ans = min(px[-1], py[-1])
        break

print(ans)