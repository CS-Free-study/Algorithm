import sys
from collections import deque
input = sys.stdin.readline

for _ in range(int(input())):
    s = input().rstrip()
    l, r = deque(), deque()

    for i in s:
        if i == '<':
            if l:
                r.appendleft(l.pop())
        elif i == '>':
            if r:
                l.append(r.popleft())
        elif i == '-':
            if l:
                l.pop()
        else:
            l.append(i)
    
    print(''.join(l + r))