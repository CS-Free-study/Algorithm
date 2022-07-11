#1158 요세푸스 문제
# 실버 4
import sys
n, k = map(int,sys.stdin.readline().split())

circle_que = [i for i in range(1, n+1)]
pop_k = []
index = 0
for i in range(n):
    index += k-1
    if len(circle_que) <= index:
        index %= len(circle_que)
    pop_k.append(circle_que.pop(index))

print('<',", ".join(map(str, pop_k)), '>',sep="")



# 1 2 3 4 5 6 7 index = 2
# 3
# 4 5 6 7 1 2 index = 4
# 6
# 7 1 2 4 5 index = 1
# 2




