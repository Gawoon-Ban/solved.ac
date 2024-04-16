import sys
input = sys.stdin.readline  

n = int(input())
dp =[0 for _ in range(n+1)]
if n == 1:
    print(0)
    sys.exit(0)
dp[2] = 3
for i in range(4,n+1,2):
    dp[i] = dp[i-2]*3 + 2
    for j in range(i-4,0,-2):
        dp[i] += dp[j]*2
print(dp[n])