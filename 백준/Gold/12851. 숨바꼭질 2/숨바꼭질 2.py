import sys
input = sys.stdin.readline
from collections import deque
"""
백준 12851 숨바꼭질 2
1. 이거 답이 1일때가 문제다. (답의 이전 값이 0 이라 모든 수가 후보군이 됨) 
일단 다른 경우도 함 봐보자     (4,5)
2. 이거 1 -> 2로 갈때도 문제다. (1에서 2로 가는 경우가 2가지가 나옴)
 (0,3)

일단 이거 2개인듯. 선대 갔다와서 고쳐보자
"""

import sys
input = sys.stdin.readline
N,K = map(int, input().split())
q = deque([N])
value = [0 for _ in range(100002)]
cnt = 0
if K == N+1:
    print(1)
    print(1)
    exit()
count = [0 for _ in range(100002)]
check = 0
while q:
    x = q.popleft()
    if x == K and check == 0:
        cnt += 1
        answer = value[x]
        continue
    elif x == K and check == 1:
        cnt += 1
        continue
    if x > 100000 or x<0:
        continue
    if x+1 < 100002:
        if value[x+1] == 0 or value[x+1] == value[x]+1:
            value[x+1] = value[x]+1
            q.append(x+1)
    if x>=1:
        if value[x-1] == 0 or value[x-1] == value[x]+1:
            q.append(x-1)
            value[x-1] = value[x]+1
    if x*2 < 100002:
        if value[x*2] == 0 or value[x*2] == value[x]+1:
            q.append(x*2)
            value[x*2] = value[x]+1
print(answer)
print(cnt)