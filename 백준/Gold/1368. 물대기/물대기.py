import sys
input = sys.stdin.readline
import heapq
"""
백준 1368 물대기

일단 모든 논을 잇거나, 물을 판다는 점에서 최소 스패닝트리가 떠오름
힙에 (거기다 우물 팔 때 드는 비용,0, 정점)항을 기존 크루스칼에서 추가한다.
"""
n = int(input().rstrip())
heap = []
for i in range(1,n+1):
    heapq.heappush(heap,(int(input().rstrip()),0,i))
for i in range(1,n+1):
    costs = list(map(int,input().split()))
    for j in range(n):
        if j != 0:
            heapq.heappush(heap,(costs[j],i,j+1))
parent = [i for i in range(n+1)]
def find (x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]
def union(x,y):
    root_x = find(x)
    root_y = find(y)
    if root_x == root_y:
        return False
    if root_x < root_y:
        parent[root_y] = root_x
    else:
        parent[root_x] = root_y
    return True
ans = 0
while heap:
    cost, x, y = heapq.heappop(heap)
    if union(x,y):
        ans += cost
print(ans)