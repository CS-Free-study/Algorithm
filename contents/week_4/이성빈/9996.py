# 백준 9996번 한국이 그리울 땐 서버에 접속하지
# SILER 3
# 알고리즘 분류 : 문자열, 브루트포스 알고리즘, 정규 표현식
N = int(input())
check = list(input().split('*'))
for _ in range(N) :
    word = input()
    val = True
    if word[:len(check[0])] != check[0]  :
        val = False
    if word[-1:-len(check[1])-1:-1] != check[1][::-1] :
        val = False
    if len(word) < len(check[0]) + len(check[1]) :
        val = False
    if val :
        print("DA")
    else :
        print("NE")