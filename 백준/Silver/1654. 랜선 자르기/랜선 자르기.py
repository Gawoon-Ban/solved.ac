import sys
input = sys.stdin.readline

def checking (list_, mid_, K_):
    answer = 0
    for i in list_:
        answer += i//mid_
    if answer >= K_:
        return True
    else:
        return False

N,K  = map(int,input().split())
cups = []
for _ in range(N):
    cup = int(input())
    cups.append(cup)

low = 0
high = max(cups)
while low != high:
    mid = (low+high+1)//2
    if checking(cups,mid,K):
        low = mid
    else:
        high = mid-1 
print(low)
