# 백준 1124번 언더프라임
# SILVER 2
# 알고리즘 분류 : 수학, 정수론, 소수 판정, 에라토스테네스의 체
A,B = map(int,input().split())
check = [0,0] + [1]*(B-1)
p = [0]*(B+1)
for i in range(2,B+1) :
    if check[i] :
        p[i] += 1
        for j in range(i*2,B+1,i) :
            check[j] = 0
            p[j] = p[j//i] + 1
ans = 0
for i in range(A,B+1) :
    if check[p[i]] :
        ans += 1
print(ans)

# 다른풀이
A,B = map(int,input().split())
check = [0,0] + [1]*(B-1)
p = []
for i in range(2,B+1) :
    if check[i] :
        p.append(i)
        for j in range(i*2,B+1,i) :
            check[j] = 0
ans = 0
for i in range(A,B+1) :
    val = i
    div = 0
    cnt = 0
    while val != 1 :
        if val%p[div] == 0 :
            val //= p[div]
            cnt += 1
        else :
            div += 1
    if cnt in p :
        ans += 1
print(ans)