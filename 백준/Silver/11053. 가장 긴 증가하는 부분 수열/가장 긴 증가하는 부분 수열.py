import sys

input = sys.stdin.readline

n = int(input())
nums= list(map(int, input().split())) 
answer = [0 for _ in range(n)]
for i in range(n):
    answer[i] = 1
    for j in range(i):
        if nums[j] < nums[i]:
            answer[i] = max(answer[i],answer[j]+1)
print(max(answer))