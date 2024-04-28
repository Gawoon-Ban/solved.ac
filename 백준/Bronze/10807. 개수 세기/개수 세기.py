n = int(input())
nums = list(map(int,input().split()))
ans = 0
goal = int(input())
for i in nums:
    if i == goal:
        ans += 1
print(ans)