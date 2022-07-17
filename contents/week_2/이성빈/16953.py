# 백준 16953번 A -> B
# SILVER 2
# 알고리즘 분류 : 그래프
# 처음에 check 리스트를 활용해서 했을 때 메모리 초과가 났음 
# 메모리를 줄이기 위해 변수 하나에 횟수를 저장시키고 도착하면 출력하게 만듬.
from collections import deque
A,B = map(int,input().split())
q = deque()
q.append([A,0])
while q :
    a,m = q.popleft()
    if a == B :
        print(m+1)
        exit()
    for i in range(2) :
        if i == 0 :
            a_ = a*10 + 1
        else :
            a_ = a*2
        if a_ > B :
            continue
        q.append([a_,m+1])
print(-1)