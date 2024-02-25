import sys
from itertools import combinations

def all_nums(n,m):
    nums = [i for i in range(1,n+1)]
    for comb in combinations(nums,m):
        yield list(comb)



input = sys.stdin.readline
N,M = map(int,input().split())
for i in all_nums(N,M):
    for j in i:
        print(j,end=' ')
    print()