import sys
from itertools import permutations

input = sys.stdin.readline

n,m = map(int,input().split())
nums = list(map(int,input().split()))

def all_nums(nums):
    for i in set(permutations(nums,m)):
        yield i

for i in sorted(all_nums(nums)):
    print(' '.join(map(str,i)))