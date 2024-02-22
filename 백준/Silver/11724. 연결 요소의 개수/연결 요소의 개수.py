import sys

input = sys.stdin.readline
N,M = map(int,input().split())
visited = [0] * (N+1)
lines = [[] for _ in range(N+1)]
for i in range(M):
    u,v = map(int,input().split())
    lines[u].append(v)
    lines[v].append(u)

answer = 0
for i in range(1,N+1):
    if visited[i] == 0:
        visited[i] = 1
        answer +=1
        q = [i]
        while len(q) != 0:
            pos = q.pop(0)
            for j in lines[pos]:
                if visited[j] == 0:
                    visited[j] = 1
                    q.append(j)
print(answer)