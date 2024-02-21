def U (board):

    #가로로 리스트들이 묶여 있던 기존의 board를 기존 board에서 세로위치에 있는 원소끼리 모이도록 새로운 new_board를 작성
    new_board = []
    for b in range(8):
        new_line = []
        for o in range(8):
            new_line.append(board[o][b])
        new_board.append(new_line)
    
    #0을 제거한 새로운 reduced_board를 얻는다
    reduced_board = []
    for i in range(8):
        reduced_line = []
        for  j in range(8):
            if new_board[i][0] == 0 and new_board[i][1] == 0 and new_board[i][2] == 0 and new_board[i][3] == 0 and new_board[i][4] == 0 and new_board[i][5] == 0 and new_board[i][6] == 0 and new_board[i][7] == 0:
                reduced_line.append(0)
            elif new_board[i][j] != 0 :
                reduced_line.append(new_board[i][j])
        reduced_board.append(reduced_line)

    new_board2= []
    for q in reduced_board:
        r = len(q)
        e = 0
        while e < r-1:
                if q[e] == q[e+1]:
                    q[e] *= 2
                    q.pop(e+1)
                    r -= 1
                e += 1
        new_board2.append(q)

    for t in new_board2:
        while len(t) < 8:
            t.append(0)

    for f in range(8):
        for h in range(8):
            board[f][h] = new_board2[h][f]
    return(board)

def D (board):
    new_board = []
    for b in range(8):
        new_line = []
        for o in range(7,-1,-1):
            new_line.append(board[o][b])
        new_board.append(new_line)

    reduced_board = []
    for i in range(8):
        reduced_line = []
        for  j in range(8):
            if new_board[i][0] == 0 and new_board[i][1] == 0 and new_board[i][2] == 0 and new_board[i][3] == 0 and new_board[i][4] == 0 and new_board[i][5] == 0 and new_board[i][6] == 0 and new_board[i][7] == 0:
                reduced_line.append(0)
            elif new_board[i][j] != 0 :
                reduced_line.append(new_board[i][j])
        reduced_board.append(reduced_line)
    new_board2= []
    for q in reduced_board:
        r = len(q)
        e = 0
        while e < r-1:
                if q[e] == q[e+1]:
                    q[e] *= 2
                    q.pop(e+1)
                    r -= 1
                e += 1
        new_board2.append(q)

    
    for t in new_board2:
        while len(t) < 8:
            t.append(0)
    for f in range(8):
        for h in range(8):
            board[7-h][f] = new_board2[f][h]
    return(board)
def L (board):
    reduced_board = []
    for i in range(8):
        reduced_line = []
        for  j in range(8):
            if board[i][0] == 0 and board[i][1] == 0 and board[i][2] == 0 and board[i][3] == 0 and board[i][4] == 0 and board[i][5] == 0 and board[i][6] == 0 and board[i][7] == 0:
                reduced_line.append(0)
            elif board[i][j] != 0 :
                reduced_line.append(board[i][j])
        reduced_board.append(reduced_line)

    new_board= []

    for q in reduced_board:
        r = len(q)
        e = 0
        while e < r-1:
                if q[e] == q[e+1]:
                    q[e] *= 2
                    q.pop(e+1)
                    r -= 1
                e += 1
        new_board.append(q)

    for t in new_board:
        while len(t) < 8:
            t.append(0)
    board = new_board
    return(board)

def R(board):

    #가로로 리스트들이 묶여 있던 기존의 board를 기존 board에서 세로위치에 있는 원소끼리 모이도록 새로운 new_board를 작성
    new_board = []
    for b in range(8):
        new_line = []
        for o in range(7,-1,-1):
            new_line.append(board[b][o])
        new_board.append(new_line)
    
    #0을 제거한 새로운 reduced_board를 얻는다
    reduced_board = []
    for i in range(8):
        reduced_line = []
        for  j in range(8):
            if new_board[i][0] == 0 and new_board[i][1] == 0 and new_board[i][2] == 0 and new_board[i][3] == 0 and new_board[i][4] == 0 and new_board[i][5] == 0 and new_board[i][6] == 0 and new_board[i][7] == 0:
                reduced_line.append(0)
            elif new_board[i][j] != 0 :
                reduced_line.append(new_board[i][j])
        reduced_board.append(reduced_line)

    new_board2= []
    for q in reduced_board:
        r = len(q)
        e = 0
        while e < r-1:
                if q[e] == q[e+1]:
                    q[e] *= 2
                    q.pop(e+1)
                    r -= 1
                e += 1
        new_board2.append(q)

    
    for t in new_board2:
        while len(t) < 8:
            t.append(0)

    for f in range(8):
        for h in range(8):
            board[f][h] = new_board2[f][7-h]
    return(board)

def print_board(board):
    for i in range(8):
        for j in range(8):
            if j == 7:
                print(board[i][j])
            else:
                print(board[i][j], end= " ")

board1 = []
for _ in range(8):
    line = map(int,input().split())
    board1.append(list(line))

commander = input()
if commander == "U":
    print_board(U(board1))
elif commander == "D":
    print_board(D(board1))
elif commander == "L":
    print_board(L(board1))
else:
    print_board(R(board1))