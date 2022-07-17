# 백준 1747번 소수&팰린드롬
# SILVER 1
# 알고리즘 분류 : 수학, 브루트포스, 정수론, 소수 판정, 에라토스테네스의 체
# 백만일때 소수를 구하는것을 생각못해서 첫 제출에서 틀렸음, 백만을 고려하고 제출했을때 정답
N = int(input())
n = 1003002
check = [1]*n
m = int(n**0.5)
for i in range(2,m+1) :
    if check[i] :
        for j in range(i*2,n,i) :
            check[j] = 0
prime_list = [i for i in range(2,n) if check[i]]
def check_fel(i) :
    i = str(i)
    len_i = len(i)
    if len_i % 2 :
        if i[:len_i//2] == i[len_i-1:len_i//2:-1] :
            return True
    else :
        if i[:len_i//2] == i[len_i-1:len_i//2-1:-1] :
            return True
    return False
for i in prime_list :
    if i >= N and check_fel(i) :
        print(i)
        break