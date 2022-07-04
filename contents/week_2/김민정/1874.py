# 1874 스택 수열(문제 이해 어려움)
# 스택 이용, 실버 2

n = int(input())
check = True
ans = []
stack = []
cnt = 1

for i in range(n):
    a = int(input())
    while cnt <= a :
        stack.append(cnt)
        ans.append('+')
        cnt += 1
    if stack[-1] == a:
        stack.pop()
        ans.append('-')
    else:
        check = False
        break

if check:
    for i in ans:
        print(i)
else:
    print("no")









