import sys
input = sys.stdin.readline

"""
백준 10942 팰린드롬?

팰린드롬 = 중앙을 기준으로 대칭
S~E까지가 팰린드롬인지 확인

당연히 그냥 노말하게 해봣는데 시간 터졌고
dp 쓸 방법 알았다
만약 1~4가 펠린드롬이라면 2~3도 펠린드롬이다
"""
N = int(input())
nums = list(map(int,input().split()))
M = int(input())
dp = [[0] *N for _ in range(N)]
def is_pan(s,e):
    for i in range((e-s+1)//2):
        if nums[s+i] != nums[e-i]:
            return False
    return True

for _ in range(M):
    S,E = map(int,input().split())
    if S == E:
        print(1)
    elif dp[S-1][E-1]:
        print(1)
    elif is_pan(S-1,E-1):
        while S<=E:
            dp[S-1][E-1] = 1
            S += 1
            E -= 1
        print(1)
    else:
        print(0)