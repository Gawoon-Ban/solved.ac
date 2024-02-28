import sys
import heapq
input = sys.stdin.readline

"""
백준 1753 최단경로
걍 다익 쓰면 되지 않나? 일단 다익을 쓸건데, 두 정점 사이에 여러 간선이 있을 수 있다는 걸 주의
얘는 애초에 입력 받을때, 만약 이미 있으면, 더 작은 w로 갱신
마지막 INF까지 다익 빼박임
"""

INF = int(1e9)
V,E = map(int,input().split())
start = int(input())
graph = [[] for _ in range(V+1)]

def search(u_,v_,graph):
    index = 0
    for i in graph[u_]:
        if i[1] == v_:
            return index
        index += 1
    return -1


for _ in range(E):
    u,v,w = map(int,input().split())
    ind = search(u,v,graph)
    if ind != -1 :
        if graph[u][ind][0] > w:
            graph[u][ind][0] = w
    else:
        graph[u].append([w,v])
distance = [INF] * (V+1)
visited = [0] * (V+1)

def dijkstra(start):
    q = []
    heapq.heappush(q,(0,start))
    distance[start] = 0
    while q:
        dist , pos = heapq.heappop(q)
        if visited[pos] == 1:
            continue
        visited[pos] = 1
        for i in graph[pos]:
            cost = dist + i[0]
            if cost < distance[i[1]]:
                distance[i[1]] = cost
                heapq.heappush(q,(cost,i[1]))
dijkstra(start)
for i in range(1,V+1):
    print(distance[i] if distance[i] != INF else "INF")