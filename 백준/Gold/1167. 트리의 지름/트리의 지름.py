import sys
input = sys.stdin.readline
from collections import deque

"""
백준 1167 트리의 지름

이거 걍 이전 문제에서 입력 방식만 바뀐거 아님?
입력 받을 때만 신경쓰고 나머지는 그대로 하면 될듯

아 이거는 루트가 꼭 1이라는 말은 없네. 근데 차피 그래프로 풀건데 알빠노
이번엔 트리 지름 성질 쓴다 ㅋㅋ

(정점 , 거리)
"""

n = int(input())
graph = [[] for _ in range(n+1)]

for _ in range(n):
    lines = list(map(int,input().split()))
    a = lines[0]
    for nodes in zip(lines[1::2],lines[2::2]):
        if nodes[0] == -1:
            break
        graph[a].append(nodes)

def dfs(start):
    distance = [-1] * (n+1)
    stack = deque()
    stack.append((start,0))
    distance[start] = 0
    while stack:
        pos , dist  = stack.pop()
        for i in graph[pos]:
            cost  = dist + i[1]
            if distance[i[0]] == -1:
                distance[i[0]] = cost
                stack.append((i[0],cost))
    max_val = max(distance)
    return distance.index(max_val),max_val

max_pt = dfs(1)[0]
print(dfs(max_pt)[1])