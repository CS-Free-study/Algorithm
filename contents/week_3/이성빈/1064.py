# 백준 1064번 평행사변형
# SILVER 4
# 알고리즘 분류 : 수학, 기하학, 피타고라스 정리
from math import sqrt
x1,y1,x2,y2,x3,y3 = map(int,input().split())
length = [sqrt((x1-x2)**2 +(y1-y2)**2),sqrt((x2-x3)**2 + (y2-y3)**2),sqrt((x1-x3)**2 + (y1-y3)**2)]
length.sort()
if (y2-y1)*(x2-x3) == (y2-y3)*(x2-x1):
    print(-1.0)
    exit()
min_length = length[0]*2 + length[1]*2
max_length = length[1]*2 + length[2]*2
print(max_length - min_length)