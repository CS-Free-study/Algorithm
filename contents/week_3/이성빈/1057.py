# 백준 1057번 토너먼트
# SILVER 3
# 알고리즘 분류 : 수학, 브루트포스 알고리즘
# 총 라운드는 int(N**0.5)+1 라운드임.
# 라운드를 진행하면서 A와 B의 차이가 1이고 작은게 홀수이면 라운드를 출력
# 승리하면 받는 번호가 (A+1)//2 임
N,A,B = map(int,input().split())
for i in range(1,int(N**0.5)+2) :
    if abs(A-B) == 1 and min(A,B)%2 :
        print(i)
        exit()
    A = (A+1)//2
    B = (B+1)//2
