import sys
input = sys.stdin.readline

n = int(input())
nums = sorted(list(map(int, input().split())))
x = int(input())

answer = 0
left, right = 0, n-1 
while left < right:
    temp = nums[left] + nums[right]
    if temp == x:
        answer += 1
        left += 1
    elif temp < x:
        left += 1
    else:
        right -= 1
print(answer)