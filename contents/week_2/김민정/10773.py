#10773 제로 - 실버4

k = int(input())
arr = []
cnt = 0

for _ in range(k):
    n = int(input())
    if n == 0:
        cnt -= arr.pop()

    else:
        arr.append(n)
        cnt += n
print(cnt)

