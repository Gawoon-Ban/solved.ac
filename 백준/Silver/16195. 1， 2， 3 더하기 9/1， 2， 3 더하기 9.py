import sys

input = sys.stdin.readline


T = int(input())

dp = [[0 for _ in range(1001)] for _ in range(1001)]

dp[0][0] = 1

for i in range(1, 1001):
    for j in range(1, 1001):
        if i>= 1:
            dp[i][j] += dp[i-1][j-1]
        if i>= 2:
            dp[i][j] += dp[i-2][j-1]
        if i>= 3:
            dp[i][j] += dp[i-3][j-1]
        dp[i][j] %= 1000000009

for _ in range(T):
    answer = 0
    N, M = map(int, input().split())
    for i in range(M+1):
        answer += dp[N][i]
    print(answer % 1000000009)