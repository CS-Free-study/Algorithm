# 백준 1032번 명령프롬프트
# BRONZE 1
# 알고리즘 분류 : 구현, 문자열
# 전수조사해서 문자가 다른경우에는 ? 로 치환해준다.

N = int(input())
li = [list(input()) for _ in range(N)]
idx = []
for i in range(N) :
    for j in range(N) :
        for k in range(len(li[0])) :
            if li[i][k] != li[j][k] :
                li[i][k] = '?'
print(''.join(li[0]))