import sys
input = sys.stdin.readline
from collections import deque

"""
백준 14567 선수과목
일단 제목부터 위상정렬
메모이제이션 느낌으로 가면 될듯
dp에는 각 노드까지 듣는데 필요한 최소 학기 수
"""

n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]
indegree = [0 for _ in range(n+1)]
for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    indegree[b] += 1

q = deque()
dp = [0 for _ in range(n+1)]
for i in range(1,n+1):
    if indegree[i] == 0:
        q.append(i)
        dp[i] = 1
while q:
    pos = q.popleft()
    for next in graph[pos]:
        indegree[next] -= 1
        if indegree[next] == 0:
            q.append(next)
            dp[next] = dp[pos] + 1
for i in range(1,n+1):
    print(dp[i], end = " ")