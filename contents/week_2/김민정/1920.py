# 1920 수 찾기
# 실버 4
import sys

n = int(sys.stdin.readline())
n_arr = set(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
m_arr = list(map(int, sys.stdin.readline().split()))

n_arr.sort()

for i in m_arr:
    if i in n_arr:
        print(1)
    else:
        print(0)







