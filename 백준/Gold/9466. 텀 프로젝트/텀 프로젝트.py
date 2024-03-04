import sys
input = sys.stdin.readline
from collections import deque
"""
백준 9466 텀 프로젝트

이거 연결요소 잖아
근데 약간 다르다. ans를 연결 요소 더 할때 처럼 막 더하면 안되네. 또한
false일 경우 visited 관리도 중요하다
"""

def dfs(start,graph,visited):
    global ans
    stack = deque([start])
    
    #지금까지 지나온 길 (팀이 될 수 있는 후보들)
    route = [start]
    while stack:
        pos = stack.pop()
        visited[pos] = 1
        next = graph[pos]
        if visited[next] == 1:
            if next in route:
                ans -= len(route[route.index(next):])
                return
        else:
            stack.append(next)
            route.append(next)
    return 0

for _ in range(int(input())):
    N = int(input())
    ans = N
    arr = list(map(int,input().split()))
    visited = [0 for _ in range(N+1)]
    graph = [0] + arr
    
    for i in range(1,N+1):
        if visited[i] == 0:
            dfs(i,graph,visited)
    print(ans)