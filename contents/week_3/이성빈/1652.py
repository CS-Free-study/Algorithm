# 백준 1652번 누울 자리를 찾아라
# BRONZE 1
# 알고리즘 분류 : 문자열, 구현
N = int(input())
li = [list(input()) for _ in range(N)]
cnt_ver = 0
cnt_hor = 0
for i in range(N) :
    check = 1
    for j in range(N-1) :
        if li[i][j] == '.' and li[i][j+1] == '.' and check :
            cnt_hor += 1
            check = 0
        if li[i][j] == 'X' :
            check = 1
for i in range(N) :
    check = 1
    for j in range(N-1) :
        if li[j][i] == '.' and li[j+1][i] == '.' and check :
            cnt_ver += 1
            check = 0
        if li[j][i] == 'X' :
            check = 1
print(cnt_hor,cnt_ver)