# 10815 숫자 카드
# 이진 탐색을 이용하여 시간 단축
import sys
import math


def binarySearch(arr, target):
    start = 0
    end = len(arr)-1
    mid = math.ceil((start + end) / 2)

    while end >= start:
        if arr[mid] == target:
            return 1
        elif arr[mid] < target:
            start = mid+1
        else:
            end = mid-1
        mid = math.ceil((start + end) / 2)
    return 0


n = int(sys.stdin.readline())
n_arr = list(map(int, sys.stdin.readline().split()))

m = int(sys.stdin.readline())
m_arr = list(map(int, sys.stdin.readline().split()))

n_arr.sort()

for i in m_arr:
    a = binarySearch(n_arr, i)
    print(a,end=' ')
