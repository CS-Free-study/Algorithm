# 백준 1049번 기타줄
# SILVER 4
# 알고리즘 분류 : 수학, 그리디 알고리즘
N,M = map(int,input().split())
six = []
one = []
result = 0
for i in range(M) :
    s,o = map(int,input().split())
    six.append(s)
    one.append(o)
six.sort()
one.sort()
result += N//6*min(six[0],one[0]*6)
result += min(six[0],one[0]*(N%6))
print(result)