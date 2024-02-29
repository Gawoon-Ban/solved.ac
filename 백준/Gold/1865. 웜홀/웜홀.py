import sys
input = sys.stdin.readline

"""
백준 1865 웜홀
일단 간선에 음수 나오는 거 보니 벨포 써야함. 음수 간선은 방향 없이 두지만
일반 도로 -> 방향 있음 -> 간선 2개로 취급
문제에서 물어보는 것은 그래프에 음수 순환이 있는지를 확인하라
걍 벨포 쓰면 끝
"""

def search(u_,v_,graph):
    index = 0
    for i in graph[u_]:
        if i[1] == v_:
            return index
        index += 1
    return -1

INF = int(1e9)
TC = int(input())
answer = []

def bf(start, graph,distance):
    distance[start] = 0
    for _ in range(N-1):
        for i in range(1,N+1):
            for node in graph[i]:
                cost, to_go  = node
                cost += distance[i]
                if distance[to_go] > cost:
                    distance[to_go] = cost
    for i in range(1,N+1):
        for node in graph[i]:
            cost , to_go = node
            cost += distance[i]
            if distance[to_go] > cost:
                distance = [INF] * (N+1)
                return True
    distance = [INF] * (N+1)
    return False

for _ in range(TC):
    N,M,W = map(int,input().split())
    graph = [[] for _ in range(N+1)]
    for i in range(M):
        s,e,t = map(int,input().split())
        if search(s,e,graph) == -1:
            graph[s].append((t,e))
        else:
            if graph[s][search(s,e,graph)][0] > t:
                graph[s][search(s,e,graph)] = (t,e)
        if search(e,s,graph) == -1:
            graph[e].append((t,s))
        else:
            if graph[e][search(e,s,graph)][0] > t:
                graph[e][search(e,s,graph)] = (t,s)

    for i in range(W):
        s,e,t = map(int,input().split())
        graph[s].append((-t,e))
    distance = [INF] * (N+1)
    """
    if all(bf(i,graph,distance) for i in range(1,N+1)):
        answer.append("YES")
    else:
        answer.append("NO")
    """
    if bf(1,graph,distance):
        answer.append("YES")
    else:
        answer.append("NO")
for i in answer:
    print(i)