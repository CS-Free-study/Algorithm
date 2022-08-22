# 백준 25345번 루나의 게임 세팅
# SILVER 1
# 알고리즘 분류 : 수학, 조합론
import math
N,K = map(int,input().split())
li = list(map(int,input().split()))
print(math.comb(N,K)*2**(K-1)%(10**9+7))