import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int,input().split()))
dp = [[0] *N for _ in range(N)]

for i in range(N):
    dp[i][i] = 1
    if i < N-1:
        if nums[i] == nums[i+1]:
            dp[i][i+1] = 1
for pel_len in range(2,N):
    for i in range(N-pel_len):
        if nums[i] == nums[i+pel_len] and dp[i+1][i+pel_len-1]:
            dp[i][i+pel_len] = 1
M = int(input())
for _ in range(M):
    S,E = map(int,input().split())
    print(dp[S-1][E-1])