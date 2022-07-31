# 백준 1183번 약속
# SILVER 3
# 알고리즘 분류 : 수학, 정렬
N = int(input())
li = []
for i in range(N) :
    A,B = map(int,input().split())
    li.append(A-B)
li.sort()
if N%2 :
    print(1)
else :
    print(li[N//2] - li[N//2 - 1] + 1)