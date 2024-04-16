import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int,input().split())

superior = list(map(int,input().split()))
dp = [0 for _ in range(n+1)]
graph = [[] for _ in range(n+1)]
for i in range(1,n):
    graph[superior[i]].append(i+1)
for _ in range(m):
    i,w = map(int,input().split())
    dp[i] += w
q = deque([1])
while q:
    x = q.popleft()
    for i in graph[x]:
        dp[i] += dp[x]
        q.append(i)
print(*dp[1:])