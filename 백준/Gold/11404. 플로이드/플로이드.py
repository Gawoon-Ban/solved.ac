import sys
input = sys.stdin.readline

"""
백준 11404 플로이드

모든 정점에서 정점으로 가는 최단 거리를 구해야함
이걸 다익을 여러번 쓰는 경우 시간이 더 오래걸리기에 플로이드 워셜을 사용
이건 3중 for문을 이용하여 구하며, 
"""

INF = int(1e9)
n = int(input())
m = int(input())
graph = [[INF] *(n+1) for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1,n+1):
        if i==j:
            graph[i][j] = 0
            break

for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a][b] = min(graph[a][b],c)

for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            graph[i][j] = min(graph[i][j],graph[i][k]+graph[k][j])

for i in range(1,n+1):
    for j in range(1,n+1):
        if graph[i][j] == INF:
            print(0,end=' ')
        else:
            print(graph[i][j],end=' ')
    print()