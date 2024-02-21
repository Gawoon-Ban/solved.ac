import sys
from collections import defaultdict
input = sys.stdin.readline
N= int(input())
nums = list(map(int,input().split()))
nums_dict = defaultdict(int)
for i in nums:
    nums_dict[i] += 1
keys = sorted(nums_dict.keys())
index_ = len(keys)
for i in keys:
    nums_dict[i] = len(keys) -index_
    index_ -= 1
for i in nums:
    print(nums_dict[i], end = " ")
