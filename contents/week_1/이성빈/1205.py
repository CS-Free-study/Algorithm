# 백준 1205번 등수 구하기
# SILVER 5
# 알고리즘 분류 : 구현
# 리스트에서 같은 수가 있으면 같은수가 몇개인지 세고 자기보다 작은수가 나오면 그 수 앞에 넣는다.
N,S,P = map(int,input().split())
if N > 0 :
    li = list(map(int,input().split()))
index = N+1
cnt = 0
for i in range(N) :
    if S == li[i] :
        cnt += 1
    if S > li[i] :
        li.insert(i,S)
        index = i+1
        break
if index <= P :
    print(index-cnt)
else :
    print(-1)