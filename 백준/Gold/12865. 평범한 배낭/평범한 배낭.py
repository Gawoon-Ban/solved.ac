import sys

input = sys.stdin.readline

"""
백준 12865 평범한 배낭

w = 무게, V = 가치, K = max 무게
"""
N,K = map(int, input().split())
dp = [[0 for _ in range(100001)] for _ in range(101)]
W = []
V = []

for _ in range(N):
    w,v = map(int, input().split())
    W.append(w)
    V.append(v)

for i in range(1,N+1):
    for j in range(0,K+1):
        if W[i-1] <=j:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-W[i-1]]+V[i-1])
        else:
            dp[i][j] = dp[i-1][j]
print(dp[N][K])