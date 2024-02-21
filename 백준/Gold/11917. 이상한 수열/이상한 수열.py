import sys
def find (nums, target):
    nums.sort()
    for i in nums:
        if i>= target:
            return i
    return False
input = sys.stdin.readline
dicts = {}
n = int(input())
nums = list(map(int,input().split()))
m = int(input())
if m <= n:
    nums = list(nums)
    print(nums[m-1])
else:
    for i in nums:
        dicts[i] = 1
    a = len(dicts)
    b = find(nums,a)
    if b:
       if m >=n+ (b-a) +1:
            print(b)
       else:
            print(a+m-n-1)
    else:
        value = len(dicts)
        for _ in range(m-n-1):
            value +=1
        print(value)  