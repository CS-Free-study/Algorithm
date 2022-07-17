# 백준 25335번 Gravity Hackenbush
# SILVER 5
# 알고리즘 분류 : 그리디 알고리즘, 게임 이론
import sys
input = sys.stdin.readline
N,M = map(int,input().split())
li = [input() for _ in range(N)]
order = [0,0,0]
for _ in range(M) :
    a,b,c = map(str,input().split())
    if c == 'R' :
        order[0] += 1
    elif c == 'B' :
        order[1] += 1
    else :
        order[2] += 1
if order[2]%2 :
    if order[1] - order[0] > 0 :
        check = 0
    else :
        check = 1
else :
    if order[0] - order[1] > 0 :
        check = 1
    else :
        check = 0
print("jhnah917" if check else "jhnan917")