import sys
input = sys.stdin.readline
from collections import deque
"""
백준 25545 MMST

일단 "모든 간선의 가중치가 다른 무향 연결 그래프"를 강조한 것에서 힌트를 받아
최소와 최대를 구해, 그들의 가중치와 사용한 간선 번호를 저장, 
그리고 최소에서 안 쓴 간선 한개와 최대에서 안 쓴 간선 한개씩 가져옴
그리고 걔네 둘을 포함해서 MST 돌리면 되지 않을까 싶은
"""
def find(x,parent):
    if parent[x] != x:
        parent[x] = find(parent[x],parent)
    return parent[x]

def union(x,y,parent):
    root_x = find(x,parent)
    root_y = find(y,parent)
    if root_x == root_y:
        return False
    if root_x < root_y:
        parent[root_x] = root_y
    else:
        parent[root_y] = root_x
    return True

n,m = map(int, input().split())
if n-1 == m:
    print("NO")
    sys.exit(0)
edges = []

for i in range(1,m+1):
    a,b,c = map(int, input().split())
    edges.append((c,a,b,i))

###############################################################
minimum_edge = sorted(edges)
moderate_edge = deque(minimum_edge[:])
minimum_edge = deque(minimum_edge)
min_edges = {}
edge_1 = 0
min_parent= [i for i in range(n+1)]
while minimum_edge:
    weight,x,y,edge_num = minimum_edge.popleft()
    if union(x,y,min_parent):
        min_edges[edge_num] = 1
        continue
    edge_1 = (weight,x,y,edge_num)
###############################################################
moderate_edge.appendleft(edge_1)
parent = [i for i in range(n+1)]
print("YES")
while moderate_edge:
    weight,x,y,edge_num = moderate_edge.popleft()
    if union(x,y,parent):
        print(edge_num,end=" ")