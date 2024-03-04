import sys
input = sys.stdin.readline
from collections import deque

"""
백준 2252 줄 세우기

일단 어떤 우선순위? 순서가 정해져있기에 위상정렬 사용
"""

n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]
indegree = [0 for _ in range(n+1)]
answer = deque()

for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    indegree[b] += 1
q = deque()
for i in range(1,n+1):
    if indegree[i] == 0:
        q.append(i)
while q:
    pos = q.popleft()
    answer.append(pos)
    for i in graph[pos]:
        indegree[i] -= 1
        if indegree[i] == 0:
            q.append(i)
for i in answer:
    print(i,end = " ")