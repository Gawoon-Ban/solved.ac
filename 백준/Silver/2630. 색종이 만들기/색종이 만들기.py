import sys

input = sys.stdin.readline

N = int(input())
papers = []
for _ in range(N):
    papers.append(list(map(int, input().split())))

num_1 = 0
num_0 = 0

def answering(size,x,y):
    global num_1
    global num_0
    color = papers[y][x]
    for i in range(size):
        for j in range(size):
            if color != papers[y+i][x+j]:
                answering(size//2,x,y)
                answering(size//2,x+size//2,y)
                answering(size//2,x,y+size//2)
                answering(size//2,x+size//2,y+size//2)
                return
    if color == 1:
        num_1 += 1
    else:
        num_0 += 1
answering(N,0,0)
print(num_0)
print(num_1)