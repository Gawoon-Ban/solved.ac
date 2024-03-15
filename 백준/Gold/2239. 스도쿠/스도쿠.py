import os, io, sys
#input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
input = sys.stdin.readline
"""
백준 2239 스도쿠

일단 사전순이 힌트였음. 좌->우, 위-> 아래순으로 탐색할건데, 만약 0을 만나면 탐색을 돌림
for문을 돌려 1~9까지 넣어보고 만약 가능하면 그 숫자를 두고 다음 칸으로 넘어감.
만약 불가능하다면 다음 숫자로 넘어감
위의 check과정은 가로줄,세로줄, square 체크 함수를 만들어 체크함
O(N^2)인데 해봤자 N이 9라 충분히 가능할듯
만약 위치가 (n-1,n-1)까지 왔다면 스도쿠를 print하고 sys.exit(0)
"""
sdoku = [list(input().strip()) for _ in range(9)]

def check_row(y,board,num):
    if num in board[y]:
        return False
    return True

def check_column(x,board,num):
    for i in range(9):
        if board[i][x] == num:
            return False
    return True

def check_square(x,y,board,num):
    x_start = (x//3)*3
    y_start = (y//3)*3
    for i in range(3):
        for j in range(3):
            if board[y_start+i][x_start+j] == num:
                return False
    return True

def solve(x,y,board):
    copy_board = [board[i][:] for i in range(9)]  
    if x == 0 and y == 9:
        for i in range(9):
            for j in range(9):
                print(board[i][j],end="")
            print()
        sys.exit(0)
    if board[y][x] == "0":
        for i in range(1,10):
            i = str(i)
            if check_row(y,board,i) and check_column(x,board,i) and check_square(x,y,board,i):
                copy_board[y][x] = i
                if x == 8:
                    solve(0,y+1,copy_board)
                else:
                    solve(x+1,y,copy_board)
    else:
        if x == 8:
            solve(0,y+1,copy_board)
        else:
            solve(x+1,y,copy_board)
solve(0,0,sdoku)