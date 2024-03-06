import os, io, sys
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
from collections import deque

"""
백준 1005 ACM Craft

일단 건물 지을 때 순서가 있고, 하위 건물이 존재 -> 위상 정렬
이거 오늘 풀었던 위상문제중에 dp있던거랑 비슷한거 같은데
dp[n]은 n번째 건물을 짓는 데까지 걸리는 최소 시간
"동시에 건물을 지을 수 있다" 에 집중하여 코드를 짜보자
"""

for _ in range(int(input())):
    n,k = map(int,input().split())

    # 시간을 저장
    time = [0] + list(map(int,input().split()))
    graph = [[] for _ in range(n+1)]

    # 진입차수 저장
    indegree = [0 for _ in range(n+1)]

    #dp[n]은 n번호 건물을 짓는데 걸리는 최소 시간
    dp = [0 for _ in range(n+1)]
    for _ in range(k):
        a,b = map(int,input().split())
        graph[a].append(b)
        indegree[b] += 1
    w = int(input())
    q = deque()

    #진입 차수가 0인 노드를 전부 넣는다
    for i in range(1,n+1):
        if indegree[i] == 0:
            q.append(i)
            dp[i] = time[i]
    
    #q에 있는 노드들을 bfs로 돌림
    while q:
        pos = q.popleft()
        for i in graph[pos]:
            indegree[i] -= 1
            dp[i] = max(dp[i],dp[pos] + time[i])
            if indegree[i] == 0:
                q.append(i)
    print(dp[w])