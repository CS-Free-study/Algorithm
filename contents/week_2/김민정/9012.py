# 9012 괄호
# 스택 문제


def string_test(s):
    cnt = 0
    if len(s) % 2 == 1:
        return 0
    for i in s:
        if i == ")" and cnt == 0:
            return 0
        elif i == "(":
            cnt += 1
        elif i == ")":
            cnt -= 1
    if cnt == 0:
        return 1
    else:
        return 0

t = int(input())
arr = []
cnt = 0

for _ in range(t):
    s = input()
    arr.append(s)

for i in arr:
    if string_test(i) == 0:
        print("No")
    else:
        print("Yes")





