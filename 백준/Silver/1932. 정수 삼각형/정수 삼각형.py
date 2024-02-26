import sys

input = sys.stdin.readline

"""
백준 1932 정수 삼각형

이건 대놓고 dp임 ㅋㅋ
dp[n][k]로 하면 n번째 층에서 k번째 애를 골랐을 때, 그 경로의 최댓값
이러면 dp 점화식은 k==0, k==(n-1), 그 외로 나눠야 함
전자 2개는 걍 외곽선으로 쭉 더해야함
후자는 dp[n][k] = max(dp[n-1][k-1],dp[n-1][k]) + arr[n][k]
"""

n = int(input())

triangle = [list(map(int,input().split())) for _ in range(n)]
dp = [[0]*n for _ in range(n)]

dp[0][0] = triangle[0][0]
for i in range(n):
    for j in range(i+1):
        if j == 0:
            dp[i][0] = dp[i-1][0] + triangle[i][0]
        elif j == i:
            dp[i][j] = dp[i-1][j-1] + triangle[i][j]
        else:
            dp[i][j] = max(dp[i-1][j-1],dp[i-1][j]) + triangle[i][j]
if n==1:
    print(triangle[0][0])
else:
    print(max(dp[n-1]))