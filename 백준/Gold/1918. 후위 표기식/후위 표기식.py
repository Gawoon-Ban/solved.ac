import sys
input = sys.stdin.readline
from collections import deque

q = deque()
pre_not = input().strip()
for i in pre_not:
    if i.isalpha():
        print(i, end="")
    elif i == '(':
        q.append(i)
    elif i == '+' or i == '-':
        while q and q[-1] != '(':
            print(q.pop(), end="")
        q.append(i)
    elif i == '*' or i =='/':
        while q and (q[-1] == '*' or q[-1] == '/'):
            print(q.pop(),end ="")
        q.append(i)
    elif i == ')':
        while q and q[-1] != '(':
            print(q.pop(), end="")
        q.pop()
while q:
    print(q.pop(), end="")