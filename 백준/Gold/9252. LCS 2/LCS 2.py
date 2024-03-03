import sys
input = sys.stdin.readline
from collections import deque
"""
백준 9252 LCS 2
자자 최장 공통 부분 수열이 또 왔어요.

아 얘는 LCS 여러개 중에 하나를 출력해야하네
일단 dp와 길이는 LCS와 같고
출력은 dp[n][m]을 기준으로 거꾸로 간다
dp[n-1][m],dp[n][m-1]중 dp[n][m]이랑 같은게 있으면 그쪽으로
없다면 현재 문자 출력 후 -> dp[n-1][m-1]로 이동
이대로 dp[0][0]까지 가면 된다. 
"""

str1 = input().strip()
str2 = input().strip()
n = len(str1)
m = len(str2)
dp = [[0 for _ in range(m+1)] for __ in range(n+1)]

for i in range(1,n+1):
    for j in range(1,m+1):
        if str1[i-1] == str2[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
LCS = dp[n][m]
print(LCS)
answer = deque()
def find_lcs(n,m,lcs):
    if lcs == 0:
        return
    if dp[n-1][m] == lcs:
        find_lcs(n-1,m,lcs)
    elif dp[n][m-1] == lcs:
        find_lcs(n,m-1,lcs)
    else:
        answer.appendleft(str1[n-1])
        find_lcs(n-1,m-1,lcs-1)
find_lcs(n,m,LCS)
print(''.join(answer))