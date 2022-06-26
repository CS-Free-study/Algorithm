# 백준 1946번 신입 사원
# SILVER 1
# 알고리즘 분류 : 그리디 알고리즘, 정렬
# 1차 점수가 가장 높은 사람을 기준으로 2차 점수가 높은사람들을 합격시킨다.
import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T) :
    li = []
    N = int(input())
    cnt = 1
    for i in range(N) :
        li.append(list(map(int,input().split())))
    li.sort()
    val = li[0][1]
    for i in range(1,N) :
        if val > li[i][1] :
            cnt += 1
            val = li[i][1]
    print(cnt)