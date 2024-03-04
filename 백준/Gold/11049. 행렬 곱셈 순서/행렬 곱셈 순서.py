import sys
input = sys.stdin.readline

"""
백준 11049 행렬 곱셈 순서

dp를 2차원 배열로 만들어보자
dp[i][j] = i~j번째 행렬들을 곱하는데 필요한 최소 연산 횟수
dp[i][j]  = i~j 사이에 있는 k로 잘라. 그리고 그 둘을 곱할 때 드는 연산횟수 + 그 둘 각각의 연산횟수
            이게 단순히 dp[i][k] + dp[k][j]로 쪼개면 안된다.
            dp[i][k] + dp[k+1][j] + matrix[i][0] * matrix[k][1] * matrix[j][1]
이렇게 나눠야함
+ 행렬이 3개까지 연결된것도 칸을 미리 채워둠. 
"""

N = int(input())
INF = 2**31
dp = [[0 for _ in range(N)] for _ in range(N)]
matrix = list(list(map(int,input().split())) for _ in range(N))

for gap in range(1,N):
    for j in range(N-gap):
        row = j
        col = j + gap
        if gap == 1:
            dp[row][col] = matrix[row][0] * matrix[row][1] * matrix[col][1]
            continue
        """
        if gap == 2:
            dp[row][col] = min(dp[row][col-1] + matrix[row][0] * matrix[col-1][1] * matrix[col][1],dp[row+1][col] + matrix[row][0] * matrix[row+1][0] * matrix[col][1])
            continue
        """
        dp[row][col] = INF
        for k in range(row,col):
            dp[row][col] = min(dp[row][col], dp[row][k]+ dp[k+1][col] + matrix[row][0] * matrix[k][1]* matrix[col][1])
print(dp[0][N-1])