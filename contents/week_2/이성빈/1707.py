# 백준 15829번 Hashing
# Bronze 2
# 알고리즘 분류 : 문자열, 해싱
N = int(input())
li = list(input())
res = 0
for i in range(N) :
    res += ((ord(li[i])-96)*31**i)
print(res%1234567891)