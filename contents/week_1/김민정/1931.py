# 1931 회의실 배정
# 1개의 회의실을 사용하고자 하는 N개의 회의에 대한 회의실 사용표
# 그리디 알고리즘 2 (11047번 참고,그리디 알고리즘 1)

N = int(input())
using_time = []

for _ in range(N):
    start, end = map(int, input().split())
    using_time.append([start, end])

using_time.sort(key=lambda ut : ut[0])
using_time.sort(key=lambda ut : ut[1])

time = 0
count = 0

for i in range(N):
    if time <= using_time[i][0]:
        time = using_time[i][1]
        count += 1
        print(time)

print(count)





