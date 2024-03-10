import sys
input = sys.stdin.readline

n = int(input())
num = list(map(int,input().split()))
k = int(input())

new_num = []

ans = 0  
sigma = 0 

for i in num:
    sigma += i
    new_num.append(sigma)

for i in range(n-1,-1,-1):
    j = 0
    if new_num[i] > k:
        ans += 1
    while new_num[i]-new_num[j] > k:
        ans += 1
        j += 1
print(ans)