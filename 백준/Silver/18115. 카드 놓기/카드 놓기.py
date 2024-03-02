import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
answer = deque()
command = list(map(int,input().split()))
stack = deque(command)

#이번에 넣을 카드
number = 1

while stack:
    command = stack.pop()
    if command == 1:
        answer.appendleft(number)
    elif command == 2:
        first_card = answer.popleft()
        answer.appendleft(number)
        answer.appendleft(first_card)
    else:
        answer.append(number)
    number += 1
for i in answer:
    print(i,end = " ")