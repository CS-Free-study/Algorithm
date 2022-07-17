# 백준 1991번 트리 순회
# SILVER 1
# 알고리즘 분류 : 트리, 재귀
# 트리를 딕셔너리로 만들고 재귀를 통해 각 노드를 출력함.


N = int(input())
tree = {}
for _ in range(N) :
    P,L,R = map(str,input().split())
    tree[P] = [L,R]
def pre(root) :
    if root != '.' :
        print(root,end='')
        pre(tree[root][0])
        pre(tree[root][1])
def ino(root) :
    if root != '.' :
        ino(tree[root][0])
        print(root,end='')
        ino(tree[root][1])
def post(root) :
    if root != '.' :
        post(tree[root][0])
        post(tree[root][1])
        print(root,end='')
pre('A')
print()
ino('A')
print()
post('A')