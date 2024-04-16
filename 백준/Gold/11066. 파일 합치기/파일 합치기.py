import sys
input = sys.stdin.readline

for _ in range(int(input())):
    K = int(input())
    pages = list(map(int, input().split()))
    dp = [[0 for _ in range(K)] for _ in range(K)]

    for i in range(K-1):
        dp[i][i+1] = pages[i] + pages[i+1]
    for space in range(2,K):
        for i in range(K-space):
            j = i + space
            dp[i][j] = min([dp[i][k] + dp[k+1][j] for k in range(i,j)]) + sum(pages[i:j+1])
    print(dp[0][K-1])