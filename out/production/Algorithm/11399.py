# 11399 ATM - 인출하는데 걸리는 시간의 최소값 구하기
# 그리디 알고리즘 3
n = int(input())
p = list(map(int, input().split()))

p.sort()
total = 0
for i in range(n+1):
    hap = 0
    for j in range(0,i):
        hap += p[j]
    total += hap

print(total)