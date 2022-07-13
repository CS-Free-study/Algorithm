# 백준 18111번 마인크래프트
# SILVER 2
# 알고리즘 분류 : 구현, 브루트포스 알고리즘
# Python 3로 제출하니 시간초과가 났음. Pypy3로 제출
import sys
input = sys.stdin.readline
N,M,B = map(int,input().split())
time_ans = sys.maxsize
height = 0
li = [list(map(int,input().split())) for _ in range(N)]
for selected in range(257) :
    block_val = B
    time_val = 0
    for i in range(N) :
        for j in range(M) :
            val = li[i][j]
            if selected > val :
                time_val += selected - val
                block_val -= selected - val
            else :
                time_val += (val - selected) * 2
                block_val += val - selected
    if block_val < 0 :
        continue
    if time_ans >= time_val :
        time_ans = time_val
        height = selected
print(time_ans,height)