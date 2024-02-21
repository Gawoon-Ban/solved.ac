import sys
input = sys.stdin.readline
from collections import defaultdict
n,x = map(int,input().split())
visitors = list(map(int,input().split()))
first = 0
for i in range(x):
    first += visitors[i]
sums_ = defaultdict(int)
sums_[first] +=1
left = 0
right = x-1
for _ in range(1,n-x+1):
        if x == 1:
             max_ = max(visitors)
             sums_[max_] = 1
        else:
             first = first + visitors[right+1] - visitors[left]
             left += 1
             right += 1
             sums_[first] +=1
sums = []
for i in sums_:
    sums.append(i)
if x == n:
     max_ = sum(visitors)
     print(max_)
     print(1)
else:
     max_ = max(sums)
     if max_ == 0:
        print("SAD")
     elif x == n:
        pass
     else:
        print(max_)
        print(sums_[max_])
