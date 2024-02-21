import sys
from collections import deque
input = sys.stdin.readline

def d_c():
    dq = deque([(0,N)])
    while dq:
        for _ in range(len(dq)):
            start,end = dq.popleft()
            if end - start <= 1:
                continue
            mid = (start + end) // 2
            for i in range(start,mid):
                m_team[i] = "A"
            for i in range(mid,end):
                m_team[i] = "B"
            dq.append((start,mid))
            dq.append((mid,end))
        answer.add("".join(m_team))

N = int(input())
m_team = ["A" for _ in range(N)]
answer = set()
d_c()
for i in answer:
    print(i)
for _ in range(7-len(answer)):
    print("A"+("B"*(N-1)))