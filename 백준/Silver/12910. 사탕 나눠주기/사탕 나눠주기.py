import sys
from collections import Counter
 
input = sys.stdin.readline

N = int(input())
nums  = list(map(int, input().split()))

answer = 0
count = Counter(nums)
mul = 1
for i in range(1,max(nums)+1):
    if count[i] == 0:
        break
    else:
        mul *= count[i]
        answer += mul
print(answer)

