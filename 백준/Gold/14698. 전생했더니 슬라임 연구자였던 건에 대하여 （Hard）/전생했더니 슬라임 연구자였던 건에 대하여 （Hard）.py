import sys
import heapq
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    n = int(input())
    answer = 1
    nums = list(map(int,input().split()))
    heapq.heapify(nums)
    while len(nums) > 1:
        least1 = heapq.heappop(nums)
        least2 = heapq.heappop(nums)
        new = least1*least2
        answer *= new
        heapq.heappush(nums,new)
    print(answer%1000000007)