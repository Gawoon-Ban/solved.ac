import sys
input = sys.stdin.readline
"""
백준 13460 구슬 탈출 2

2048과 비슷하게 구현
구슬을 움직이면 벽을 만날때까지 이동. 만나면 그 앞 위치까지 이동
if 갈 경로에 구멍이 있으면 돌린 횟수를 출력

함수 4개의 작동과정은 매우 유사하다 
"""
n,m = map(int, input().split())
board = [list(input().strip()) for _ in range(n)]
INF = int(1e9)
def move_up(r_x,r_y,b_x,b_y,cnt):

    success = 0
    # 두 구슬이 같은 경로상에 있고, 파란 구슬이 더 위에 있을 때
    if r_x == b_x and r_y > b_y:
        while board[b_y-1][b_x] != '#':
            if board[b_y-1][b_x] == 'O':
                return -1
            b_y -= 1
        while board[r_y-1][r_x] != '#' and r_y - 1 > b_y:
            if board[r_y-1][r_x] == 'O':
                return cnt+1
            r_y -= 1

    # 두 구슬이 같은 경로상에 있고, 빨간 구슬이 더 위에 있을 때
    elif r_x == b_x and r_y < b_y:
        while board[r_y-1][r_x] != '#':

            #구멍 - 빨간 구슬 - 벽 - 파란구슬 같은 경우를 해결하기 위해 success라는 변수를 사용, 만약 파란 공도 다 굴렸는데 얘는 구멍에 안 빠지면 cnt+1을 리턴
            #또한 빨간 공이 구멍에 빠지면 얘의 좌표를 INF나 -2로 바꿔서 파란공이 움직일 때 제약이 없도록 한다.
            if board[r_y-1][r_x] == 'O':
                success = 1
                r_y = -2
                break
            r_y -= 1

        while board[b_y-1][b_x] != '#' and r_y < b_y-1:
            if board[b_y-1][b_x] == 'O':
                return -1
            b_y -= 1
        if success == 1:
            return cnt+1

    # 두 구슬이 다른 경로상에 있을 때
    else:
        #파란 공을 먼저 돌려서 빨간 공이 빠지든 말든, 파란공이 빠졌으면 -1 리턴
        while board[b_y-1][b_x] != '#':
            if board[b_y-1][b_x] == 'O':
                return -1
            b_y -= 1
        while board[r_y-1][r_x] != '#':
            if board[r_y-1][r_x] == 'O':
                return cnt+1
            r_y -= 1
    return r_x,r_y,b_x,b_y,cnt+1

def move_down(r_x,r_y,b_x,b_y,cnt):
    success = 0
    # 두 구슬이 같은 경로상에 있고, 파란 구슬이 더 아래에 있을 때
    if r_x == b_x and r_y < b_y:

        #파란공은 빠지면 그냥 끝이니까 빨간 공이 어떻든 -1 리턴
        while board[b_y+1][b_x] != '#':
            if board[b_y+1][b_x] == 'O':
                return -1
            b_y += 1
        while board[r_y+1][r_x] != '#' and r_y+1 < b_y:
            if board[r_y+1][r_x] == 'O':
                return cnt+1
            r_y += 1

    # 두 구슬이 같은 경로상에 있고, 빨간 구슬이 더 아래에 있을 때
    elif r_x == b_x and r_y > b_y:
        # 얘도 파란공 - 벽 - 빨간공 - 구멍의 경우를 고려하여 success 변수 사용
        while board[r_y+1][r_x] != '#':
            if board[r_y+1][r_x] == 'O':
                success = 1
                r_y = INF
                break
            r_y += 1
        while board[b_y+1][b_x] != '#' and b_y+1 < r_y:
            if board[b_y+1][b_x] == 'O':
                return -1
            b_y += 1
        if success == 1:
            return cnt+1
    # 두 구슬이 다른 경로상에 있을 때
    else:
        while board[b_y+1][b_x] != '#':
            if board[b_y+1][b_x] == 'O':
                return -1
            b_y += 1
        while board[r_y+1][r_x] != '#':
            if board[r_y+1][r_x] == 'O':
                return cnt+1
            r_y += 1
    return r_x,r_y,b_x,b_y,cnt+1

def move_left(r_x,r_y,b_x,b_y,cnt):
    success = 0
    # 두 구슬이 같은 경로상에 있고, 파란 구슬이 더 왼쪽에 있을 때
    if r_y == b_y and r_x > b_x:
        while board[b_y][b_x-1] != '#':
            if board[b_y][b_x-1] == 'O':
                return -1
            b_x -= 1

        while board[r_y][r_x-1] != '#' and r_x-1 > b_x:
            if board[r_y][r_x-1] == 'O':
                return cnt+1
            r_x -= 1

    # 두 구슬이 같은 경로상에 있고, 빨간 구슬이 더 왼쪽에 있을 때
    elif r_y == b_y and r_x < b_x:
        while board[r_y][r_x-1] != '#':
            if board[r_y][r_x-1] == 'O':
                success = 1
                r_x = -2
                break
            r_x -= 1
        while board[b_y][b_x-1] != '#' and r_x < b_x-1: 
            if board[b_y][b_x-1] == 'O':
                return -1
            b_x -= 1
        if success == 1:
            return cnt+1

    # 두 구슬이 다른 경로상에 있을 때
    else:
        while board[b_y][b_x-1] != '#':
            if board[b_y][b_x-1] == 'O':
                return -1
            b_x -= 1
        while board[r_y][r_x-1] != '#':
            if board[r_y][r_x-1] == 'O':
                return cnt+1
            r_x -= 1

    return r_x,r_y,b_x,b_y,cnt+1

def move_right(r_x,r_y,b_x,b_y,cnt):
    success = 0
    # 두 구슬이 같은 경로상에 있고, 파란 구슬이 더 오른쪽에 있을 때
    if r_y == b_y and r_x < b_x:
        while board[b_y][b_x+1] != '#':
            if board[b_y][b_x+1] == 'O':
                return -1
            b_x += 1
        while board[r_y][r_x+1] != '#' and r_x+1 < b_x:
            if board[r_y][r_x+1] == 'O':
                return cnt+1
            r_x += 1

    # 두 구슬이 같은 경로상에 있고, 빨간 구슬이 더 오른쪽에 있을 때
    elif r_y == b_y and r_x > b_x:
        while board[r_y][r_x+1] != '#':
            if board[r_y][r_x+1] == 'O':
                success = 1
                r_x = INF
                break
            r_x += 1
        while board[b_y][b_x+1] != '#' and r_x > b_x+1:
            if board[b_y][b_x+1] == 'O':
                return -1
            b_x += 1
        if success == 1:
            return cnt+1
    # 두 구슬이 다른 경로상에 있을 때
    else:
        while board[b_y][b_x+1] != '#':
            if board[b_y][b_x+1] == 'O':
                return -1
            b_x += 1
        while board[r_y][r_x+1] != '#':
            if board[r_y][r_x+1] == 'O':
                return cnt+1
            r_x += 1
    return r_x,r_y,b_x,b_y,cnt+1

red_x = 0
red_y = 0
blue_x = 0
blue_y = 0
for i in range(n):
    for j in range(m):
        if board[i][j] == 'R':
            red_x = j
            red_y = i
        elif board[i][j] == 'B':
            blue_x = j
            blue_y = i

answer =[]
def simulation(r_x,r_y,b_x,b_y,cnt):
    if cnt == 10:
        return
    for i in range(4):
        if i==0:
            new = move_up(r_x,r_y,b_x,b_y,cnt)
            if type(new) == int:
                if new != -1:
                    answer.append(new)
            elif type(new) == tuple:
                r_x_,r_y_,b_x_,b_y_,cnt_ = new
                simulation(r_x_,r_y_,b_x_,b_y_,cnt_)
                
        elif i==1:
            new = move_down(r_x,r_y,b_x,b_y,cnt)
            if type(new) == int:
                if new != -1:
                    answer.append(new)
            elif type(new) == tuple:
                r_x_,r_y_,b_x_,b_y_,cnt_ = new
                simulation(r_x_,r_y_,b_x_,b_y_,cnt_)

        elif i==2:
            new = move_left(r_x,r_y,b_x,b_y,cnt)
            if type(new) == int:
                if new != -1:
                    answer.append(new)
            elif type(new) == tuple:
                r_x_,r_y_,b_x_,b_y_,cnt_ = new
                simulation(r_x_,r_y_,b_x_,b_y_,cnt_)

        elif i==3:
            new = move_right(r_x,r_y,b_x,b_y,cnt)
            if type(new) == int:
                if new != -1:
                    answer.append(new)
            elif type(new) == tuple:
                r_x_,r_y_,b_x_,b_y_,cnt_ = new
                simulation(r_x_,r_y_,b_x_,b_y_,cnt_)
                
simulation(red_x,red_y,blue_x,blue_y,0)
if len(answer) == 0:
    print(-1)
else:
    print(min(answer))