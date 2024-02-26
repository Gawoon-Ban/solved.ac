import sys

input = sys.stdin.readline

"""
백준 11660 구간 합 구하기 5

일단 2차원 배열을 받아. 그리고 이제 2차원 dp를 만들건데, dp[n][k]는 n번재 줄에 있는 애들 중
k번째 애까지의 합으로 정의한다. 그리고 이제 dp[n][k] = dp[n][k-1] + arr[n][k]로 정의한다.
"""

N,M = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]

dp = [[0] *(N) for _ in range(N)]
for i in range(N):
    for j in range(N):
        if j == 0:
            dp[i][j] = arr[i][j]
        else:
            dp[i][j] = dp[i][j-1] + arr[i][j]

for _ in range(M):
    x1,y1,x2,y2 = map(int,input().split())
    x1 -= 1
    y1 -= 1
    x2 -= 1
    y2 -= 1
    answer = 0
    for i in range(x1,x2+1):
        if y1 == 0:
            answer += dp[i][y2]
        else:
            answer += dp[i][y2] - dp[i][y1-1]
    print(answer)