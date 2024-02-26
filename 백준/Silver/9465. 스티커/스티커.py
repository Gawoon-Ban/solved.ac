import sys

input = sys.stdin.readline

"""
백준 9465 스티커

일단 저 크기와 똑같은 배열을 가져와
그리고 n번째 열의 칸은 1~ n-1 열까지의 스티커와 그 칸까지 뜯었을 때의 점수
하고 max 때려서 구하면 어캐 되지 않을까? 싶은
"""

T = int(input())
for _ in range(T):
    n = int(input())
    stickers = [list(map(int,input().split())) for _ in range(2)]
    dp = [[0]*n for _ in range(2)]
    for i in range(n):
        for j in range(2):
            if i==0:
                dp[j][0] = stickers[j][0]
                continue
            if i == 1:
                dp[j][1] = stickers[j][1] + dp[1-j][0]
                continue
            dp[j][i] = stickers[j][i] + max(dp[1-j][i-1],dp[j][i-2],dp[1-j][i-2])
    print(max(dp[0][n-1],dp[1][n-1]))