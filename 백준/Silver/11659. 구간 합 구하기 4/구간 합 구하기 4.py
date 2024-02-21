import sys
input = sys.stdin.readline

n,m = map(int,input().split())
nums = list(map(int,input().split()))
order = []
for _ in range(m):
    new_order = map(int,input().split())
    order.append(new_order)
sums = [nums[0]]
for i in range(n):
    if i == 0:
        continue
    else:
        sums.append(sums[i-1] + nums[i])

for i in order:
    start,end = i
    if start == 1:
        print(sums[end-1])
    elif start == end:
        print(nums[end-1])
    else:
        print(sums[end-1]-sums[start-2])