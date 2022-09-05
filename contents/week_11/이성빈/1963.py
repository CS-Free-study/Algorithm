# 백준 1963번 소수 경로
# GOLD 4
# 알고리즘 분류 : 수학, 그래프 이론, 그래프 탐색, 정수론, 너비 우선 탐색, 소수 판정, 에라토스테네스의 체
import sys
from collections import deque
input = sys.stdin.readline
prime = [1]*10000
for i in range(2,101) :
    if prime[i] :
        for j in range(2*i,10000,i) :
            prime[j] = 0
def bfs(v) :
    q = deque()
    check = [0]*10000
    q.append([v,0])
    check[v] = 1
    while q :
        v,c = q.popleft()
        if v == s :
            return c
        d1 = v//1000
        d2 = v//100 - d1*10
        d3 = v//10 - d1*100 - d2*10
        d4 = v%10
        for i in range(4) :
            val = [d1,d2,d3,d4]
            for j in range(10) :
                val[i] = j
                v_ = int(''.join(list(map(str,val))))
                if v_ < 1000 or not prime[v_] :
                    continue
                if not check[v_] :
                    q.append([v_,c+1])
                    check[v_] = 1
    return 'Impossible'


T = int(input())
for _ in range(T) :
    f,s = map(int,input().split())
    print(bfs(f))