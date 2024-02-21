import sys
sys.setrecursionlimit(100000)

input = sys.stdin.readline

def DFS(x,y,h):
    for i in range(4):
        new_x = x + dx[i]  
        new_y = y + dy[i]
        if 0<=new_x< N and 0<=new_y<N and graph[new_x][new_y] > h and not no_sinked[new_x][new_y]:
            no_sinked[new_x][new_y] = True
            DFS(new_x,new_y,h)

N = int(input())
graph = []
dx = [0,0,1,-1]
dy = [1,-1,0,0]
for i in range(N):
    graph.append(list(map(int,input().split())))
answer = 1

for k in range(1,max(map(max,graph))):    
    count  = 0
    no_sinked = [[False for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if graph[i][j] > k and not no_sinked[i][j]:
                no_sinked[i][j] = True
                DFS(i,j,k)
                count += 1
    answer = max(answer,count)
print(answer)