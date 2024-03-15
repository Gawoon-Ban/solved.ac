import sys
#input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
input = sys.stdin.readline
"""
백준 9328 열쇠

일단 key를 리스트에 모으고
bfs로 돌다가 열쇠를 먹으면 열쇠를 맵에서 지우고 열쇠 추가, visited 초기화
또한 first_in에 있는 애들을 큐에 넣어줌 
문을 만나면 열쇠 여부에 따라 큐에 넣는 여부가 결정
서류를 만나면 계속

만약 탐색을 하는데 먹을 수 있는 열쇠가 없거나 + 탐색 다 했으면 종료
"""
from collections import deque
from collections import defaultdict
answers= []
for _ in range(int(input())):
    answer = 0
    h,w = map(int, input().split())
    area = [list(input().strip()) for _ in range(h)]
    keys = list(input().strip())
    if keys[0] == '0':
        keys = []
    first_in = []
    first_in_alpha = defaultdict(list)
    for i in range(0,w):
        if area[0][i] == ".":
            first_in.append((0,i))
        if area[h-1][i] == ".":
            first_in.append((h-1,i))
        if area[0][i].isalpha():
            if area[0][i].isupper():
                if area[0][i].lower() in keys:
                    first_in.append((0,i))
                else:
                    first_in_alpha[area[0][i]].append((0,i))
            else:
                first_in.append((0,i))
                keys.append(area[0][i])
                if area[0][i].upper() in first_in_alpha:
                    for door in first_in_alpha[area[0][i].upper()]:
                        first_in.append(door)
                area[0][i] = "."
        if area[h-1][i].isalpha():
            if area[h-1][i].isupper():
                if area[h-1][i].lower() in keys:
                    first_in.append((h-1,i))
                else:
                    first_in_alpha[area[h-1][i]].append((h-1,i))
            else:
                first_in.append((h-1,i))
                keys.append(area[h-1][i])
                if area[h-1][i].upper() in first_in_alpha:
                    for door in first_in_alpha[area[h-1][i].upper()]:
                        first_in.append(door)
                area[h-1][i] = "."
        if area[0][i] == "$":
            answer += 1
            area[0][i] = "."
            first_in.append((0,i))
        if area[h-1][i] == "$":
            answer += 1
            area[h-1][i] = "."
            first_in.append((h-1,i))
    for i in range(1,h-1):
        if area[i][0] == ".":
            first_in.append((i,0))
        if area[i][w-1] == ".":
            first_in.append((i,w-1))
        if area[i][0].isalpha():
            if area[i][0].isupper():
                if area[i][0].lower() in keys:
                    first_in.append((i,0))
                else:
                    first_in_alpha[area[i][0]].append((i,0))
            else:
                first_in.append((i,0))
                keys.append(area[i][0])
                if area[i][0].upper() in first_in_alpha:
                    for door in first_in_alpha[area[i][0].upper()]:
                        first_in.append(door)
                area[i][0] = "."
        if area[i][w-1].isalpha():
            if area[i][w-1].isupper():
                if area[i][w-1].lower() in keys:
                    first_in.append((i,w-1))
                else:
                    first_in_alpha[area[i][w-1]].append((i,w-1))
            else:
                first_in.append((i,w-1))
                keys.append(area[i][w-1])
                if area[i][w-1].upper() in first_in_alpha:
                    for door in first_in_alpha[area[i][w-1].upper()]:
                        first_in.append(door)
                area[i][w-1] = "."
        if area[i][0] == "$":
            answer += 1
            area[i][0] = "."
            first_in.append((i,0))
        if area[i][w-1] == "$":
            answer += 1
            area[i][w-1] = "."
            first_in.append((i,w-1))
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    visited = [[0 for _ in range(w)] for _ in range(h)]
    q = deque()
    for i in first_in:
        q.append(i)
        visited[i[0]][i[1]] = 1
    while q:
        y_pos,x_pos = q.popleft()
        for i in range(4):
            ny = y_pos + dy[i]
            nx = x_pos + dx[i]
            if ny < 0 or nx < 0 or ny >= h or nx >= w:
                continue
            if visited[ny][nx] == 1:
                continue
            if area[ny][nx] == "*":
                continue
            if area[ny][nx] == "$":
                answer += 1
                area[ny][nx] = "."
                visited[ny][nx] = 1
                q.append((ny,nx))
                continue
            if area[ny][nx].isalpha():
                if area[ny][nx].isupper():
                    if area[ny][nx].lower() in keys:
                        visited[ny][nx] = 1
                        q.append((ny,nx))
                    else:
                        continue
                else:
                    if area[ny][nx] in keys:
                        visited[ny][nx] = 1
                        area[ny][nx] = "."
                        q.append((ny,nx))
                        continue
                    else:
                        keys.append(area[ny][nx])
                        visited = [[0 for _ in range(w)] for _ in range(h)]
                        q = deque()
                        if area[ny][nx].upper() in first_in_alpha:
                            for door in first_in_alpha[area[ny][nx].upper()]:
                                first_in.append(door)
                            area[ny][nx] = "."
                        for i in first_in:
                            q.append(i)
                            visited[i[0]][i[1]] = 1
                        continue
            if area[ny][nx] == ".":
                visited[ny][nx] = 1
                q.append((ny,nx))
    answers.append(answer)

for i in answers:
    print(i)