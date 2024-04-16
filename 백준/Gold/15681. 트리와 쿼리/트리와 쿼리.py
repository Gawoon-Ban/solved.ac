import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n,r,q = map(int,input().split())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

dp = [0] * (n+1)

def solve(x):
    dp[x] = 1
    for i in graph[x]:
        if not dp[i]:
            solve(i)
            dp[x] += dp[i]
solve(r)

for _ in range(q):
    x = int(input())
    print(dp[x])