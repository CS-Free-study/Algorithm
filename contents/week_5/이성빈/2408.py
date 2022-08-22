# 백준 2408 큰 수 계산
# BRONZE 2
# 알고리즘 분류 : 수학, 구현, 사칙연산, 임의 정밀도/큰 수 연산
N = int(input())
li = []
li2 = []
li.append(int(input()))
for _ in range(N-1) :
    cmd = input()
    num = int(input())
    if cmd == '*' :
        li[-1] *= num
    elif cmd =='/' :
        li[-1] //= num
    else :
        li.append(num)
        li2.append(cmd)
ans = li[0]
for i in range(len(li2)) :
    if li2[i] == '+' :
        ans += li[i+1]
    else :
        ans -= li[i+1]
print(ans)


# 다른 풀이
N = int(input())
a = ""
for _ in range(2*N-1) :
    a += input()
a.replace("/","//")
print(eval(a))