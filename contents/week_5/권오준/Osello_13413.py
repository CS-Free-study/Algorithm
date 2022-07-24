# 백준 13413, 오셀로 재배치, 실버4
import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    a = input().rstrip()
    b = input().rstrip()

    white = 0
    black = 0

    for i in range(n):
        if a[i] != b[i]:
            if a[i] == 'W':
                white += 1
            else:
                black += 1
    
    print(max(white, black))