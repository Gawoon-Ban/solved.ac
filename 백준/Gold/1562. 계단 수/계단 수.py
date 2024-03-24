import sys
input = sys.stdin.readline
"""
백준 1562 계단 수

list 인덱스에 비트 수를 넣어도 되는 구나
리스트 -> 1<<10 같은 비트수로 표시하기
dp[n][k][bitmask] = 길이는 n, 마지막 수는 k, 사용한 수는 bitmask로 표시
"""

n = int(input())
dp = [[[0]*1024 for _ in range(10)] for _ in range(n+1)]
if n <= 9:
    print(0)
    sys.exit(0)
for i in range(1, 10):
    dp[1][i][1<<i] = 1
for i in range(2, n+1):
    for j in range(10):
        for k in range(1<<10):
            if j == 0:
                dp[i][j][k | 1<<j] += dp[i-1][j+1][k]
            elif j == 9:
                dp[i][j][k | 1<<j] += dp[i-1][j-1][k]
            else:
                dp[i][j][k | 1<<j] += dp[i-1][j-1][k] + dp[i-1][j+1][k]
            dp[i][j][k | 1<<j] %= 1000000000
ans = 0
for j in range(10):
    ans += dp[n][j][1023]
    ans %= 1000000000
print(ans)