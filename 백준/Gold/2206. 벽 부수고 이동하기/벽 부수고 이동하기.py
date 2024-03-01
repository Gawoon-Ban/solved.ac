import sys
input = sys.stdin.readline
from collections import deque
"""
백준 2206 벽 부수고 이동하기

이거 답이 안나옴 ㅋㅋ 어캐함
일단 시작위치와 끝나는 위치는 좌측 상단, 우측 하단으로 정해져있음
breakable이라는 변수를 만들어서 얘가 1이면 벽을 부술 수 있도록

일단 처음 생각은 존나 오류가 생김
그래서 만약 1을 만나면 그 자리에서 bfs를 한번 더 돌리도록 함. 근데 이러면 시간초과
음...

bfs 그 자리에서 또 쓰는 이유 -> breakable을 저장하기 위해서
그럼 다음 노드로 넘어갈 때마다 함수를 부르면 되지

사실 그전의 내 코드도 잘 돌아는 가지만, visited를 복사하는 과정에서 시간이 굉장히 소요된다. 

와 ㅅㅂ 3차원 배열? ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ
이건 진짜 생각도 못했네
"""

n,m = map(int,input().split())

graph = [list(map(int,input().strip())) for _ in range(n)]
visited = [[[False]* 2 for _ in range(m)] for _ in range(n)]
# 이렇게 3차원 배열을 만들어, 첫번째는 벽 안 부쉈을 때 그 위치의 dist
# 두번째는 벽을 부쉈을 때 그 위치의 dist

dx = [-1,1,0,0]
dy = [0,0,-1,1]
def bfs ():
    q = deque()
    q.append((0,0,1,1))
    visited[0][0][1] = True
    while q:
        x,y,breakable,distance = q.popleft()
        if x == m-1 and y == n-1:
            return distance
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or nx>=m or ny<0 or ny>=n:
                continue
            if visited[ny][nx][breakable]:
                continue
            if graph[ny][nx] == 0:
                visited[ny][nx][breakable] = True
                q.append((nx,ny,breakable,distance+1))
            elif graph[ny][nx] == 1:
                if breakable == 1:
                    visited[ny][nx][0] = True
                    q.append((nx,ny,0,distance+1))
                else:
                    continue
    return -1

print(bfs())