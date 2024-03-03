import sys
input = sys.stdin.readline

"""
백준 7579 앱
아니 이거 메모리 초과가 계속 나는데, dp를 할 때 필요한 최소의 리스트만 써도 난다
아마 m이 천만이고 그걸 최대 100까지 곱하면 10억이니 터질만 한듯

-> 그럼 코스트를 인자로 돌리자
dp[n][c] = 1~n까지의 앱을 봤고, 그 중 c만큼 비용을 썼을때, 최대로 free 할 수 있는 메모리
이러면 c는 최대 100까지니까 100곱해도 만임. 설마 이건 안터지겠지
그러고 이제 dp[N][c] 들 중 값이 M 넘는 것들 중 최소 c
"""
N,M = map(int,input().split())
memory = list(map(int,input().split()))
cost = list(map(int,input().split()))

dp = [[0 for _ in range(10001)] for __ in range(N+1)]
for n in range(1,N+1):
    for c in range(10001):
        if c < cost[n-1]:
            dp[n][c] = dp[n-1][c]
        else:
            dp[n][c] = max(dp[n-1][c], dp[n-1][c - cost[n-1]] + memory[n-1])
print(min([c for c in range(10001) if dp[N][c] >= M]))