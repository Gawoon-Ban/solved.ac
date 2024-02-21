import sys
import heapq
input = sys.stdin.readline
N = int(input())
board = []
for _ in range(N):
    line = list(map(int,input().split()))
    board.append(line)
board = sorted(board, key = lambda x :(x[0],x[1]))
heap =[]
heapq.heappush(heap, board[0][1])
for i in range(N):
    if i == 0:
        continue
    else:
        if board[i][0] < heap[0]:
            heapq.heappush(heap,board[i][1])
        else:
            heapq.heappop(heap)
            heapq.heappush(heap,board[i][1])
print(len(heap))