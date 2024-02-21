import sys
input = sys.stdin.readline

N,K = map(int,input().split())
multiple = 1
for i in range(N,N-K,-1):
    multiple = multiple * i
    
divise = 1
for i in range(1,K+1):
    divise = divise * i
    
print(int(multiple / divise))