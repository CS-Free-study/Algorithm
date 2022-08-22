# 백준 1235번 학생 번호
# SILVER 4
# 알고리즘 분류 : 구현, 문자열
N = int(input())
li = [input() for _ in range(N)]
for k in range(1,len(li[0])+1) :
    a = set(li[i][-k:] for i in range(N))
    if len(a) == N :
        print(k)
        break