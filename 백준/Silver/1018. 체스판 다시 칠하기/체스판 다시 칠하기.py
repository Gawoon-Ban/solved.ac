import sys
input = sys.stdin.readline

def is_chess (list_):
    check1 = 0
    check2 = 0
    solution1 = [list("WBWBWBWB"),list("BWBWBWBW"),list("WBWBWBWB"),list("BWBWBWBW"),list("WBWBWBWB"),list("BWBWBWBW"),list("WBWBWBWB"),list("BWBWBWBW")]
    solution2 = [list("BWBWBWBW"),list("WBWBWBWB"),list("BWBWBWBW"),list("WBWBWBWB"),list("BWBWBWBW"),list("WBWBWBWB"),list("BWBWBWBW"),list("WBWBWBWB")]
    for i in range(8):
        for j in range(8):
            if list_[i][j] != solution1[i][j]:
                check1 += 1
            elif list_[i][j] != solution2[i][j]:
                check2 += 1
    return min(check1, check2)


N,M = map(int,input().split())
board = []
point = []
for l in range(N):
    line = list(input())
    board.append(line)

for i in range(0,N-7):
    for j in range(0,M-7):
        checking = [board[x][j:j+8] for x in range(i, i+8)]
        point.append(is_chess(checking))
        
print(min(point))