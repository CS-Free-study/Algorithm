# 백준 1620, 나는야 포켓몬 마스터 이다솜, 실버4
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
pocketmons = {}

for i in range(1, n + 1):
    pocketmon = input().rstrip()
    pocketmons[i] = pocketmon
    pocketmons[pocketmon] = i

for i in range(m):
    question = input().rstrip()
    if question.isdigit():
        print(pocketmons[int(question)])
    else:
        print(pocketmons[question])
