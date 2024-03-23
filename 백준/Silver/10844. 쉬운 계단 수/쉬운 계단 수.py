import sys
input = sys.stdin.readline
"""
백준 10844 쉬운 계단 수

dp[i][j] = 길이가 i고, 마지막 숫자가 j인 계단 수의 개수
dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1](단 0,9는 예외로 따로 처리해준다.)
계단 수를 풀기 전 dp 점화식 생각하려고 푼 문제
"""
n = int(input())
dp = [[0]*10 for _ in range(n+1)]
for i in range(1, 10):
    dp[1][i] = 1
for i in range(2, n+1):
    for j in range(10):
        if j == 0:
            dp[i][j] = dp[i-1][1]
        elif j == 9:
            dp[i][j] = dp[i-1][8]
        else:
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]
print(sum(dp[n])%1000000000)