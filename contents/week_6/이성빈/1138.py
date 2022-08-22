# 백준 1138번 한 줄로 서기
# SILVER 2
# 알고리즘 분류 : 구현
N = int(input())
li = list(map(int,input().split()))
ans = []
for i in range(N-1,-1,-1) :
    ans.insert(li[i],i+1)
print(*ans)