#2750 번 :  수 정렬하기
# N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.
# 선택 정렬(Selection Sort),버블 정렬(Bubble Sort) 사용

def selectionSort(list):
    for i in range(len(list)):
        for j in range(i, len(list)):
            if list[i] > list[j]:
                list[j], list[i] = list[i], list[j]
    return list

def bubbleSort(list):
    for i in range(len(list)):
        for j in range(len(list)-1):
            if list[j+1] < list[j]:
                list[j], list[j+1] = list[j+1], list[j]
    return list

N = int(input())
arr = []
for i in range(N):
    arr.append(int(input()))
arr = bubbleSort(arr)
for i in range(len(arr)):
    print(arr[i])







