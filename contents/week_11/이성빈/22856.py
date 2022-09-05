# 백준 22856번 트리 순회
# GOLD 4
# 알고리즘 분류 : 그래프 이론, 그래프 탐색, 트리
import sys
sys.setrecursionlimit(10**8)
input = sys.stdin.readline
N = int(input())
tree = {}
cnt = -1
right = 0
for _ in range(N) :
    P,L,R = map(int,input().split())
    tree[P] = [L,R]
def ino(node,be) :
    global cnt
    global right
    cnt += 1
    if tree[node][0] != -1 :
        ino(tree[node][0],0)
    if tree[node][1] != -1 :
        if be :
            right += 1
            ino(tree[node][1],1)
        else :
            ino(tree[node][1],0)
ino(1,1)
print(cnt*2 - right)