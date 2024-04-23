import sys
import heapq
from collections import deque

input = sys.stdin.readline

while True:
    n,m = map(int,input().split())
    if n == 0 and m == 0:
        break
    
    # 다익에서 쓸 그래프
    graph = [[] for _ in range(n)]

    # 역방향 BFS를 사용할 때 쓸 그래프
    graph_inv = [[] for _ in range(n)]

    # 최단 경로를 구성하는 간선들
    least_edges = [[False for _ in range(n)] for _ in range(n)]

    s,d = map(int,input().split())
    for _ in range(m):
        u,v,p = map(int,input().split())
        graph[u].append([v,p])
        graph_inv[v].append([u,p])
    
    INF = sys.maxsize
    def dijkstra():
        distances = [INF for _ in range(n)]
        distances[s] = 0
        heap = []
        heapq.heappush(heap,[0,s])
        while heap:
            dist, pos = heapq.heappop(heap)
            if distances[pos] < dist:
                continue
            for next_pos, next_dist in graph[pos]:
                cost = dist + next_dist
                if least_edges[pos][next_pos]:
                    continue
                if distances[next_pos] > cost:
                    distances[next_pos] = cost
                    heapq.heappush(heap,[cost,next_pos])
        return distances
    mid_distances = dijkstra()
    
    def bfs():
        q = [d]
        q = deque(q)
        while q:
            pos = q.popleft()
            if pos == s:
                continue
            for pre_pos, pre_dist in graph_inv[pos]:     
                
                # 전 위치의 dist와 (전 위치 -> 현재 위치 길이)를 더한 것이 현재의 dist일 때 -> 얘는 최단경로 사용된 아이
                if mid_distances[pre_pos] + pre_dist == mid_distances[pos] and not (least_edges[pre_pos][pos]):
                    least_edges[pre_pos][pos] = True
                    q.append(pre_pos)
    bfs()
    ans_distances = dijkstra()
    if ans_distances[d] == INF:
        print(-1)
    else:
        print(ans_distances[d])