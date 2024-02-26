import sys

input = sys.stdin.readline

st1 = input().strip()
st2 = input().strip()
dp = [[0 for _ in range(len(st2)+1)] for _ in range(len(st1)+1)]

for i in range(len(st2)+1):
    for j in range(len(st1)+1):
        if i == 0 or j == 0:
            dp[j][i] = 0    
        elif st1[j-1] == st2[i-1] :
            dp[j][i] += dp[j-1][i-1] +1
        else:
            dp[j][i] = max(dp[j-1][i],dp[j][i-1])
print(max(map(max,dp)))        