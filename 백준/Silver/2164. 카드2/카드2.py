import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
cards = deque(range(1,N+1))
odd_even = 0

while len(cards) != 1:
    if odd_even % 2 ==0:
        cards.popleft()
        
    else:
        discard = cards.popleft()
        cards.append(discard)

    odd_even += 1

print(cards[0])