import sys
input = sys.stdin.readline
from collections import deque

"""
백준 2056 작업

일단 1번 작업이 진입차수가 0, 여기부터 시작
dp는 n번 작업까지 하는데 걸리는 최소 시간 

시간, 선행 노드 수, 선행 노드 
"""

n = int(input())
graph = [[] for _ in range(n+1)]
indegree = [0 for _ in range(n+1)]
time = [0 for _ in range(n+1)]
indx = 1
for _ in range(n):
    info = list(map(int,input().split()))
    time[indx] = info[0]
    if info[1] == 0:
        indx += 1
        continue
    indegree[indx] = info[1]
    for i in range(2, len(info)):
        graph[info[i]].append(indx)
    indx += 1
dp = [0 for _ in range(n+1)]
q = deque()
for i in range(1,n+1):
    if indegree[i] == 0:
        q.append(i)
        dp[i] = time[i]
while q:
    pos = q.popleft()
    for i in graph[pos]:
        indegree[i] -= 1
        dp[i] = max(dp[i], dp[pos] + time[i])
        if indegree[i] == 0:
            q.append(i)
print(max(dp))