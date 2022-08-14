# 백준 2331번 반복수열
# SILVER 3
# 알고리즘 분류 : 수학, 구현
A,P = map(int,input().split())
li = [str(A)]
ans = 0
while True :
    val = list(map(int,li[-1].rstrip()))
    sum = 0
    for i in val :
        sum += i**P
    sum = str(sum)
    if sum in li :
        print(li.index(sum) - ans)
        break
    li.append(sum)