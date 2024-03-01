import sys
input = sys.stdin.readline
from collections import deque

"""
백준 1967 트리의 지름

이거 그냥 트리의 지름이라고 말은 했는데, 각 노드당 도로가 하나인 그래프 아닌가
트리가 아닌 그냥 그래프라고 생각하고 풀자

그냥 그래프의 최대 거리를 구하는 문제라고 생각하자. 이거 플워를 써서 2차원에 max쓰면 되지 않나?
ㅋㅋ... 플워 쓰니까 메모리 터지네

다음은 이제 다익을 여러번 돌리려고 했는데, 사실 이걸로 될거였으면 플워가 댓을거임
bfs로 조지자
"""

N = int(input())
graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    a,b,c = map(int,input().split())
    graph[a].append((c,b))
    graph[b].append((c,a))

def dfs(start):
    q  = deque()
    distance = [-1] * (N+1)
    q.append((0,start))
    distance[start] = 0
    while q:
        weight, cur = q.pop()
        for i in graph[cur]:
            cost = i[0] + weight
            next = i[1]
            if distance[next] == -1 :
                distance[next] = cost
                q.append((cost,next))
    return max(distance[1:])

ans = []

for i in range(1,N+1):
    ans.append(dfs(i))
print(max(ans))