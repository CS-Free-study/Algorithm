# 백준 1141번 접두사
# SILVER 2
# 알고리즘 분류 : 문자열, 정렬
N = int(input())
li = [input() for _ in range(N)]
li.sort()
cnt = 1
for i in range(N-1) :
    if li[i] != li[i+1][:len(li[i])] :
        cnt += 1
print(cnt)