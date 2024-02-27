import sys
import heapq
input = sys.stdin.readline

"""
백준 18352 - 특정 거리의 도시 찾기
일단 다익스트라 알고리즘 문제를 풀기 전에 이 알고리즘을 익히기 위해서
일단 이 문제처럼 거리가 모두 1이여도 다익을 쓰는 거 보니, 거리의 다양성은 다익과 상관 없어 보이고
1. 출발점이 특정함
2. 최단 거리 관련 질문
이러면 다익을 쓰는 듯?
일단 바로 다익으로 거리 배열 INF로 초기화하고
O 줄이려면 heapq로 쓰고
"""

n,m,k,x  = map(int, input().split())
graph = [[] for _ in range(n+1)]
distance = [int(1e9)] * (n+1)
for i in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)

visited = [0] * (n+1)
def dijkstra(start):
    q = []
    heapq.heappush(q,(0,start))
    distance[start] = 0
    while q:
        dist, pos = heapq.heappop(q)
        if visited[pos] == 1:
            continue
        visited[pos] = 1
        for i in graph[pos]:
            if distance[i] > dist + 1:
                distance[i] = dist + 1
                heapq.heappush(q,(distance[i],i))
dijkstra(x)
if  k not in distance:
    print(-1)
else:
    for i in range(1,n+1):
        if distance[i] == k:
            print(i)