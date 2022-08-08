import sys
input = sys.stdin.readline

n = [int(input()) for _ in range(9)]
total = sum(n)

for i in range(8):
    for j in range(i + 1, 9):
        if total - n[i] - n[j] == 100:
            n.remove(n[j])
            n.remove(n[i])

            n.sort()
            print('\n'.join(map(str, n)))
            exit()
