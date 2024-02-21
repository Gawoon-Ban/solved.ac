import sys
input = sys.stdin.readline
N = int(input())
M = int(input())
poss = list(map(int,input().split()))
min1 = poss[0]
min2 = N - poss[-1]
if len(poss) > 1:
    if (poss[1]-poss[0])%2 == 1:
        min3 = (poss[1]-poss[0])//2+1
    else:
        min3 = (poss[1]-poss[0])//2
    for i in range(1,M-1):
        if (poss[i+1] - poss[i])%2 == 1:
            new_min = (poss[i+1] - poss[i])//2 + 1
        else:
            new_min = (poss[i+1] - poss[i])//2
        if new_min > min3:
            min3 = new_min
else:
    min3 = 0
real_min = max([min1,min2,min3])
print(real_min)