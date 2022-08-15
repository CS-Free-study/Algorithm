# 7568 : 덩치
# 브루트 포스 알고리즘(모든 경우의 수를 검사)

n = int(input())

group = []

for i in range(0, n):
    a, b = map(int, input().split())
    arr = [a,b]
    group.append(arr)


for i in range(0, n):
    rank = 1
    for j in range(0, n):
        if group[i][0] < group[j][0] and group[i][1]<group[j][1]:
            rank += 1
    print(rank, end=' ')
