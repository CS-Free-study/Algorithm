# 백준 25328번 다중 항목 선호도 조사 (Large)
# SILVER 3
# 알고리즘 분류 : 자료 구조, 브루트포스 알고리즘, 해시를 사용한 집합과 맵
import sys
input = sys.stdin.readline
N,M = map(int,input().split())
s = ['kor','eng','math']
f = ['apple','pear','orange']
v = ['red','blue','green']
cnt = {}
for i in s :
    for j in f :
        for k in v :
            cnt[(i,j,k)] = 0
for i in range(N) :
    a,b,c = map(str,input().split())
    cnt[(a,b,c)] += 1
for _ in range(M) :
    a,b,c = map(str,input().split())
    ans = 0
    if a == '-' :
        a = s
    else :
        a = [a]
    if b == '-' :
        b = f
    else :
        b = [b]
    if c == '-' :
        c = v
    else :
        c = [c]
    for i in a :
        for j in b :
            for k in c :
                ans += cnt[(i,j,k)]
    print(ans)