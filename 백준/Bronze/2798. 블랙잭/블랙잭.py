import sys
input = sys.stdin.readline

num, goal = map(int,input().split())
cards = list(map(int,input().split()))
sums = []
for i in range(0,num-2):
    for j in range(i+1,num-1):
        for k in range(j+1,num):
            sum = cards[i] +cards[j] + cards[k]
            sums.append(sum)
            
sums.sort(reverse = True)
for l in sums:
    if l <= goal:
        print(l)
        break