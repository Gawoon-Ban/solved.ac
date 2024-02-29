import sys
input = sys.stdin.readline

"""
백준 1991 트리 순회

여러 순회를 구현. 트리를 파이썬에서 구현할 때는 딕셔너리를 활용
여러 순회는 재귀를 통해 구현함. 정말 단순하게 탐색하는 순서대로 출력과 재귀를 돌리면 됨
"""
tree = {}
N = int(input())

for _ in range(N):
    root,left,right = input().split()
    tree[root] = (left,right)

ans_f = []
ans_m = []
ans_b = []

def pre_order(node):
    if node == ".":
        return
    ans_f.append(node)
    pre_order(tree[node][0])
    pre_order(tree[node][1])

def in_order(node):
    if node == ".":
        return
    in_order(tree[node][0])
    ans_m.append(node)
    in_order(tree[node][1])

def post_order(node):
    if node == ".":
        return
    post_order(tree[node][0])
    post_order(tree[node][1])
    ans_b.append(node)

pre_order("A")
in_order("A")
post_order("A")
print("".join(ans_f))
print("".join(ans_m))
print("".join(ans_b))