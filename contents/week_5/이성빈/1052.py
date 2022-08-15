# 백준 1052번 물병
# SILVER 1
# 알고리즘 분류 : 수학, 구현, 그리디 알고리즘, 시뮬레이션, 비트마스킹
# Python 3 시간초과 Pypy3로 제출
# 그리디 풀이
N,K = map(int,input().split())
o = N
while True :
    cnt = 0
    n = N
    while n :
        if n%2 :
            cnt += 1
        n //= 2
    if cnt <= K :
        break
    N += 1
print(N - o)

# 다른 풀이
# 이진수를 이용한 풀이
N,K = map(int,input().split())
o = N
while bin(N).count('1') > K :
    a = 2**bin(N)[::-1].index('1')
    N += a
print(N - o)