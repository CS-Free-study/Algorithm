# 백준 25329번 학생별 통화 요금 계산
# SILVER 4
# 알고리즘 분류 : 구현, 자료 구조, 정렬, 해시를 사용한 집합과 맵, 트리를 사용한 집합과 맵
import math
import sys
input = sys.stdin.readline
N = int(input())
li = []
val = []
res = []
for _ in range(N) :
    a,b = map(str,input().split())
    h,m = map(int,a.split(':'))
    time = h*60 + m
    if b in li :
        val[li.index(b)][0] += time
    else :
        li.append(b)
        val.append([time,b])
for i in val :
    if i[0] <= 100 :
        res.append([i[1],10])
    else :
        res.append([i[1],10 + math.ceil((i[0]-100)/50)*3])
res.sort(key = lambda x:(-x[1],x[0]))
for i in res :
    print(*i)