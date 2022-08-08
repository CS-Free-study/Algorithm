# 백준 11725, 트리의 부모 찾기, 실버2
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

n = int(input())
tree = [[] for _ in range(n + 1)]
parents = [0] * (n + 1)

for _ in range(1, n):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

def dfs(tree, v, parents):
    for i in tree[v]:
        if parents[i] == 0:
            parents[i] = v
            dfs(tree, i, parents)


dfs(tree, 1, parents)

for i in range(2, n + 1):
    print(parents[i])
