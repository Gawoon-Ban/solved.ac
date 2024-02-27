import sys
import heapq
input = sys.stdin.readline

"""
백준 1238 파티
일단 최장거리네. 그럼 거리를 INF가 아닌 0으로 초기화 해야 할까.
그리고 갈 때, 올 때 다익스트라 2번 쓰고 리스트 값 더해서, 최대를 골라야 할듯
"""
INF = int(1e9)
def dijkstra(start,finish):
    distance = [INF for _ in range(N+1)]
    visited = [0 for _ in range(N+1)]
    q = []
    heapq.heappush(q,(0,start))
    while q:
        dist, now = heapq.heappop(q)
        if visited[now] == 1:
            continue
        visited[now] = 1
        for i in graph[now]:
            cost = dist + i[0]
            if distance[i[1]] > cost:
                distance[i[1]] = cost
                heapq.heappush(q,(cost,i[1]))
    return distance[finish]

N,M,X = map(int,input().split())
graph = [[] for _ in range(N+1)]
times = [0 for _ in range(N+1)]
for _ in range(M):
    a,b,t = map(int,input().split())
    graph[a].append((t,b))

for i in range(1,N+1):
    if i == X:
        continue
    times[i] = dijkstra(i,X)
for i in range(1,N+1):
    if i == X:
        continue
    times[i] += dijkstra(X,i)
print(max(times))