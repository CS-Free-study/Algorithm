# 백준 25328번 문자열 집합 조합하기
# SILVER 3
# 알고리즘 분류 : 구현, 자료 구조, 문자열, 브루트포스 알고리즘
from itertools import combinations
X = list(input())
Y = list(input())
Z = list(input())
k = int(input())
res = []
li = []
X_li = list(combinations(X,k))
Y_li = list(combinations(Y,k))
Z_li = list(combinations(Z,k))
for i in X_li :
    li.append(i)
for i in Y_li :
    li.append(i)
for i in Z_li :
    li.append(i)
li.sort()
for i in range(len(li)-1) :
    if li[i] == li[i+1] :
        res.append("".join(li[i]))
res = sorted(list(set(res)))
if res :
    print(*res,sep='\n')
else :
    print(-1)