import sys
input = sys.stdin.readline
from collections import deque
"""
백준 2098 외판원 순회

dp[i][visited] = 현재 i위치, visited를 방문 했을 때, 지금까지 드는 최소비용
이때 visited는 비트마스크로 표현한다.
와 저런 동일항이 생길거라곤 상상도 못했네 ㅋㅋㅋㅋ
외판원은 진짜 나중에 다시 한번 보자
"""

n = int(input())
INF = 1e9
graph = [list(map(int, input().split())) for _ in range(n)]
dp =[[INF for _ in  range((1<<n))] for _ in range(n)]

is_visited = [[0 for _ in range(1<<n)] for _ in range(n)]

dp[0][1<<0] = 0
q = deque()
q.append((0, 1<<0))
is_visited[0][1<<0] = 1
while q:
    pos, visited = q.popleft()
    if visited == (1<<n)-1:
        continue
    for i in range(n):
        if visited & (1<<i) == 0 and graph[pos][i] != 0:
            dp[i][visited | (1<<i)] = min(dp[i][visited | (1<<i)], dp[pos][visited] + graph[pos][i])
            if(is_visited[i][visited | (1<<i)] == 0):
                q.append((i, visited | (1<<i)))
            is_visited[i][visited | (1<<i)] = 1
ans = INF
for i in range(1, n):
    if(graph[i][0] != 0):
        ans = min(ans, dp[i][(1<<n)-1] + graph[i][0])


print(ans)