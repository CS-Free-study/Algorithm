import sys
from collections import deque
input = sys.stdin.readline

r, c, n = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(r)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
q = deque()

def installBomb(graph, q):
    for x in range(r):
        for y in range(c):
            if graph[x][y] == 'O':
                q.append((x, y))

def bfs(graph, q):
    while q:
        x, y = q.popleft()
        graph[x][y] = '.'

        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y

            if 0 <= nx < r and 0 <= ny < c and graph[nx][ny] == 'O':
                graph[nx][ny] = '.'

def simulate(time):
    global graph, q
    if time == 1:
        installBomb(graph, q)
    elif time % 2 == 0:
        graph = [['O'] * c for _ in range(r)]
    else:
        bfs(graph, q)
        installBomb(graph, q)

for i in range(1, n + 1):
    simulate(i)

for i in graph:
    print(''.join(i))