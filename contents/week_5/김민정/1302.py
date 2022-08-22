# 1302 베스트셀러
# 실버 4
import sys
input = sys.stdin.readline

n = int(input())
dic = dict() # 딕셔너리 선언

for i in range(n): # n만큼 책 이름 입력 받기
    key = input()
    if key not in dic: # 만약 입력 받은 키가 딕셔너리에 존재하지 않다면
        dic[key] = 1 # 딕셔너리 값 1로 초기화
    else: # 존재한다면
        dic[key] += 1 # 딕셔너리 값에 +1

dic_max = max(dic.values()) #딕셔너리 값들 중에서 최대값 구하기
max_list = [] # 최대값의 키 리스트 선언
for k in dic: # 딕셔너리 탐색
    if dic[k] == dic_max: # 최대값을 값(value)로 가지고 있다면
        max_list.append(k) # 최대값의 키 리스트에 키 이름 추가
max_list.sort() # 키 이름을 사전 순으로 정렬
print(max_list[0]) # 가장 앞에 있는 이름 출력







