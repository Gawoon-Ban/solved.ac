import sys

input = sys.stdin.readline

n,m = map(int,input().split())
lines = []
for _ in range(m):
    lines.append(list(map(int,input().split())))
distances = [[-1]*m for _ in range(n)]
visited = [[0]*m for _ in range(n)]

zero_poses = []
for i in range(n):
    for j in range(m):
        if lines[i][j] == 2:
            start_pos = (i,j)
        if lines[i][j] == 0:
            zero_poses.append((i,j))

dx = [0,0,1,-1]
dy = [1,-1,0,0]

q = [start_pos]
sy,sx = start_pos
distances[sy][sx] = 0
visited[sy][sx] = 0
while len(q) != 0:
    y,x = q.pop(0)
    if visited[y][x] == 1:
        continue
    visited[y][x] = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= m or ny<0 or ny>=n:
            continue
        if lines[ny][nx] == 0:
            continue
        if visited[ny][nx] == 0:
            distances[ny][nx] = distances[y][x] + 1            
        q.append((ny,nx))

for _ in zero_poses:
    y,x = _
    distances[y][x] = 0
for i in distances:
    for j in i:
        print(j,end=' ')
    print()