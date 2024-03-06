
import os, io, sys
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

from collections import deque


"""
백준 2623 음악 프로그램

일단 순서가 있고, 하위 순서를 진행해야 뒤를 할 수 있다는 점에서 위상정렬
위상정렬을 돌려서 다 돌렸는데도 visited가 0인 애가 있으면 0을 출력
아닌 경우는 answer에 append 된걸 하나씩 출력
"""

n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]
indegree = [0 for _ in range(n+1)]

for _ in range(m):
    pd = list(map(int,input().split()))
    len_ = pd[0]
    for i in range(1,len_):
        graph[pd[i]].append(pd[i+1])
        indegree[pd[i+1]] += 1

q = deque()
for i in range(1,n+1):
    if indegree[i] == 0:
        q.append(i)
answer = []
while q:
    pos = q.popleft()
    answer.append(pos)
    for next in graph[pos]:
        indegree[next] -= 1
        if indegree[next] == 0:
            q.append(next)

if len(answer) != n:
    print(0)
else:
    for i in answer:
        print(i)