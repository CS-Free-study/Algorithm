# 백준 10799번 쇠막대기
# SILVER 3
# 알고리즘 분류 : 자료 구조, 스택
a = input()
stack = []
ans = 0
for i in range(len(a)) :
    if a[i] == '(' :
        stack.append("(")
    else :
        if a[i-1] == "(" :
            stack.pop()
            ans += len(stack)
        else :
            stack.pop()
            ans += 1
print(ans)