import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

dp = [[0,0] for _ in range(n+1)]
visited = [0]*(n+1)

def dfs(pos):
    visited[pos] = 1
    dp[pos][0] += 1
    for i in graph[pos]:
        if visited[i] == 0:
            dfs(i)
            dp[pos][0] += min(dp[i])
            dp[pos][1] += dp[i][0]
dfs(1)
print(min(dp[1]))