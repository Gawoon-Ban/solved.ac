import sys

input = sys.stdin.readline

n = int(input())
answer = 0
for i in range(1,n):
    point1 = 1
    point2 = point1 + i
    sum_ = int(((point1 + point2)/2)*(i+1)) 
    if sum_ > n:
        break
    elif sum_ == n:
        answer += 1
    for j in range(1,n-i):
        point1 = 1 + j
        point2 = point1 + i
        sum_ = int(((point1 + point2)/2)*(i+1))
        if sum_ > n:
            break
        elif sum_ == n:
            answer += 1
print(answer+1)