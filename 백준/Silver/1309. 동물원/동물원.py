import sys
input = sys.stdin.readline
n = int(input())
"""
dp[i][0] = i번째 행이 0,0 일때 i번째 행까지 사자를 채우는 경우의 수
dp[i][1] = i번째 행이 0,1 일때 i번째 행까지 사자를 채우는 경우의 수
dp[i][2] = i번째 행이 1,0 일때 i번째 행까지 사자를 채우는 경우의 수
"""
dp = [[0,0,0] for _ in range(n)]
dp[0][0] = 1
dp[0][1] = 1
dp[0][2] = 1
for i in range(1,n):
    dp[i][0] = (dp[i-1][0] + dp[i-1][1] + dp[i-1][2])%9901
    dp[i][1] = (dp[i-1][0] + dp[i-1][2])%9901
    dp[i][2] = (dp[i-1][0] + dp[i-1][1])%9901
print(sum(dp[n-1])%9901)