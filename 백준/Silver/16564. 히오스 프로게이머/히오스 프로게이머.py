import sys
input = sys.stdin.readline

def checking (list_, mid_, K_):
    answer = 0
    for i in list_:
        if mid_ - i <=0:
            continue
        else:
            answer += mid_ - i
    if answer > K_:
        return False
    else:
        return True

N,K  = map(int,input().split())
cups = []
for _ in range(N):
    cup = int(input())
    cups.append(cup)

low = 1
high = max(cups) + K
while low != high:
    mid = (low+high+1)//2
    if checking(cups,mid,K):
        low = mid
    else:
        high = mid -1
print(low)
