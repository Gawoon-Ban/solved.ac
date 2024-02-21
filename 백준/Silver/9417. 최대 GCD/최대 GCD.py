import math
import sys
import itertools

input = sys.stdin.readline

N = int(input())
answers = []
for _ in range(N):
    nums = list(map(int, input().split())) 
    coms = itertools.combinations(nums,2)
    gcds = []
    for com in coms:
        gcds.append(math.gcd(com[0],com[1]))
    answers.append(max(gcds))
for answer in answers:
    print(answer)