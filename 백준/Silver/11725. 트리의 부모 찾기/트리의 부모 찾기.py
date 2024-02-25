import sys

input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a] = graph[a] + [b]
    graph[b] = graph[b] + [a]
parent = [0 for _ in range(n+1)]
q = [1]
while q:
    pos = q.pop(0)
    for i in graph[pos]:
        if i == 1:
            continue
        elif parent[i] == 0:
            parent[i] = pos
            q.append(i)

for i in range(2,n+1):
    print(parent[i])