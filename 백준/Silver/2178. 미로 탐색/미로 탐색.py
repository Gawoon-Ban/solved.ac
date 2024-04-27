import sys
input = sys.stdin.readline
from collections import deque

n,m = map(int,input().split())
maps = []
for _ in range(n):
    maps.append(input().rstrip())
q = deque()
q.append((0,0,1))
dx = [0,0,1,-1]
dy = [1,-1,0,0]
visited = [[0]*m for _ in range(n)]
visited[0][0] = 1
while q:
    pos_x,pos_y,cnt = q.popleft()
    if pos_x == n-1 and pos_y == m-1:
        print(cnt)
        break
    for i in range(4):
        nx = pos_x + dx[i]
        ny = pos_y + dy[i]
        if 0<=nx<n and 0<=ny<m and visited[nx][ny] == 0 and maps[nx][ny] == '1':
            visited[nx][ny] = 1
            q.append((nx,ny,cnt+1))