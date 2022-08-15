# 백준 1206번 사람의 수
# SILVER 3
# 알고리즘 분류 : 수학, 브루트포스 알고리즘
# 사람수가 1~1000인 이유는 소수 셋째 자리 까지이기 때문
N = int(input())
li = [float(input()) for _ in range(N)]
for j in range(1,1001) :
    cnt = 0
    for i in li :
        val = int(i*j) #총점
        if int(val/j*1000)/1000 == i or int((val+1)/j*1000)/1000 == i:
            cnt += 1
    if cnt == N :
        break
print(j)