# 백준 1080번
# SILVER 1
# 알고리즘 분류 : 그리디 알고리즘
import sys
input = sys.stdin.readline
N,M = map(int,input().split())
cnt = 0
def shuffle(x,y) :
    for i in range(x,x+3) :
        for j in range(y,y+3) :
            if li1[j][i] :
                li1[j][i] = 0
            else :
                li1[j][i] = 1
li1 = [list(map(int,input().rstrip())) for _ in range(N)]
li2 = [list(map(int,input().rstrip())) for _ in range(N)]
for i in range(N-2) :
    for j in range(M-2) :
        if li1[i][j] != li2[i][j] :
            shuffle(j,i)
            cnt += 1
for i in range(N) :
    for j in range(M) :
        if li1[i][j] != li2[i][j] :
            print(-1)
            exit()
print(cnt)