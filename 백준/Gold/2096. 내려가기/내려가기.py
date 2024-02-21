import sys

N = int(input())
nums = []
for _ in range(N):
    nums.append(list(map(int,sys.stdin.readline().strip("\n").split())))
dp = [[0]*3 for _ in range(2)]
dp[0][0] = nums[0][0]
dp[0][1] = nums[0][1]
dp[0][2] = nums[0][2]
for i in range(1,N):
    dp[1][0] = max(dp[0][0],dp[0][1])+ nums[i][0]
    dp[1][1] = max(dp[0][0],dp[0][1],dp[0][2])+ nums[i][1]
    dp[1][2] = max(dp[0][1],dp[0][2])+ nums[i][2]
    dp[0][0] = dp[1][0]
    dp[0][1] = dp[1][1]
    dp[0][2] = dp[1][2]
max_num = max(dp[1][0],dp[1][1],dp[1][2])
dp = [[0]*3 for _ in range(2)]
dp[0][0] = nums[0][0]
dp[0][1] = nums[0][1]
dp[0][2] = nums[0][2]
for i in range(1,N):
    dp[1][0] = min(dp[0][0],dp[0][1])+ nums[i][0]
    dp[1][1] = min(dp[0][0],dp[0][1],dp[0][2])+ nums[i][1]
    dp[1][2] = min(dp[0][1],dp[0][2])+ nums[i][2]
    dp[0][0] = dp[1][0]
    dp[0][1] = dp[1][1]
    dp[0][2] = dp[1][2]
min_num = min(dp[1][0],dp[1][1],dp[1][2])
if N == 1:
    print(max(nums[0][0],nums[0][1],nums[0][2]),min(nums[0][0],nums[0][1],nums[0][2]))
else:
    print(max_num,min_num)