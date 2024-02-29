import sys
input = sys.stdin.readline
from collections import deque
"""
백준 13549 숨바꼭질 3
일단 bfs인데 이 문제에서 중요한 건 순간이동을 할 때 0초가 걸린다는 것
여기서 처음으로 0-1 bfs를 배운다. 
bfs기에 당연히 deque를 사용, 이것이 시간을 확 줄여준다. 
기존의 bfs처럼 하되, 일반적은 경우는 걍 뒤에 append하지만 순간이동은 앞에 넣는다.
단 이는 모두 값이 갱신되는 경우에 진행한다. 
"""
distance = [-1] * 100001

N,K = map(int,input().split())
q = deque()

def _01_bfs(N,K):
    q.append(N)
    distance[N] = 0
    while q:
        x = q.popleft()
        if x==K:
            print(distance[x])
            return 
        for nx in [x-1,x+1,2*x]:
            if 0<=nx<100001 and distance[nx] == -1:
                if nx == 2*x:
                    q.appendleft(nx)
                    distance[nx] = distance[x]
                else:
                    q.append(nx)
                    distance[nx] = distance[x] + 1
_01_bfs(N,K)