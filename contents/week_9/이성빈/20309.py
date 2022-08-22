# 백준 20309번 트리플 소트
# SILVER 3
# 알고리즘 분류 : 수학,정렬,에드훅
N = int(input())
li = list(map(int,input().split()))
for i in range(N) :
    if i%2 :
        if li[i]%2 :
            print("NO")
            exit()
    else :
        if li[i]%2 == 0 :
            print("NO")
            exit()
print("YES")