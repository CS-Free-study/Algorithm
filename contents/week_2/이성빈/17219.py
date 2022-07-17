# 백준 17219번 비밀번호 찾기
# SILVER 4
# 알고리즘 분류 : 자료 구조, 해시를 사용한 집합과 맵
# 딕셔너리를 이용해 주소와 비밀번호를 저장하고 주소값의 키를 프린트
import sys
input = sys.stdin.readline
N,M = map(int,input().split())
dic = {}
for _ in range(N) :
    a,b = map(str,input().split())
    dic[a] = b
find = [str(input().strip()) for _ in range(M)]
for i in find :
    print(dic[i])