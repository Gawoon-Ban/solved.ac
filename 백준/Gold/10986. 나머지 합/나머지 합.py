import sys
input = sys.stdin.readline
import math

n,m = map(int,input().split())
nums = list(map(int,input().split()))
s=[]
remains = {}
for i in range(m):
    remains[i] = 0
for i in range(n):
    if i == 0:
        s.append(nums[0])
        remain = nums[0]%m
        remains[remain] +=1
        
    else:
        s.append(s[i-1]+nums[i])
        remain = s[i]%m
        remains[remain] +=1
answer = 0
for i in remains:
    answer += math.comb(remains[i],2)
print(answer+remains[0])