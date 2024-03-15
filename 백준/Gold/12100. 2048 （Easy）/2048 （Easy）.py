import io,os,sys
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
#input = sys.stdin.readline
n = int(input())
def leftshift(L):
    Z = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        index = 0
        for j in range(n):
            if L[i][j] != 0:
                Z[i][index] = L[i][j]
                index += 1
    X = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        index = 0
        j = 0
        while j < n:
            if j != n-1 and Z[i][j] == Z[i][j + 1]:
                X[i][index] = Z[i][j] * 2
                index += 1
                j += 2 
            else:
                X[i][index] = Z[i][j]
                index += 1
                j += 1
    return X
um = []
for i in range(n):
    um.append(list(map(int,input().split())))
def R_shift(um):
  umr = [[0 for i in range(n)] for j in range(n)]
  for i in range(n):
      for j in range(n):
          umr[i][j] = um[i][n - j - 1]
  umr = leftshift(umr)
  board=[[0 for _ in range(n)] for _ in range(n)]
  for i in range(n):
      for j in range(n):
          board[i][j] = umr[i][n - j - 1]
  return board
def U_shift(um):
  umr = [[0 for i in range(n)] for j in range(n)]
  for i in range(n):
      for j in range(n):
          umr[i][j] = um[j][i]
  umr = leftshift(umr)
  board=[[0 for _ in range(n)] for _ in range(n)]
  for i in range(n):
      for j in range(n):
          board[i][j] = umr[j][i]
  return board
def D_shift(um):
  umr = [[0 for i in range(n)] for j in range(n)]
  for i in range(n):
      for j in range(n):
          umr[i][j] = um[n - j - 1][n - i - 1]
  umr = leftshift(umr)
  board = [[0 for _ in range(n)] for _ in  range(n)]
  for i in range(n):
      for j in range(n):
          board[i][j] = umr[n - j - 1][n - i - 1]
  return board

ans = 0
def play(cnt,board):
  if cnt == 5:
    global ans
    for i in range(n):
      ans = max(ans,max(board[i]))
    return
  for i in range(4):
    copy_board = [row[:] for row in board]
    if i==0:
      play(cnt+1,R_shift(copy_board))
    elif i == 1:
      play(cnt+1,U_shift(copy_board))
    elif i == 2:
      play(cnt+1,D_shift(copy_board))
    else:
      play(cnt+1,leftshift(copy_board))
play(0,um)
print(ans)