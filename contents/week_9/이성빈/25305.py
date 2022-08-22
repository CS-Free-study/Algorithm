# 백준 25305번 커트라인
# BRONZE 2
# 알고리즘 분류 : 구현, 정렬
N,K = map(int,input().split())
li = list(map(int,input().split()))
li.sort()
print(li[N-K])