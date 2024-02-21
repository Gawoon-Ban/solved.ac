dx = [1,0,-1,0]
dy = [0,1,0,-1]
T = int(input())
answer = []
for i in range(T):
    M,N,K = map(int, input().split())
    ground = [[0]*M for _ in range(N)]
    visited = [[0]*M for _ in range(N)]
    
    bug = 0
    for _ in range(K):
        a,b = list(map(int, input().split()))
        ground[b][a] = 1
    for j in range(N):
        for i in range(M):
            if ground[j][i] == 1 and visited[j][i] == 0:
                bug += 1
                visited[j][i] = 1
                q = [(j,i)]
                while len(q) != 0:
                    y,x = q.pop(0)
                    for k in range(4):
                        ny = y + dy[k]
                        nx = x + dx[k]
                        if 0<= ny < N and 0<= nx <M and visited[ny][nx] == 0 and ground[ny][nx] == 1:
                            q.append((ny,nx))
                            visited[ny][nx] = 1
    answer.append(bug)
for i in answer:
    print(i)