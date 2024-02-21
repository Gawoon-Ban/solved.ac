N = int(input())
nums = list(map(int,input().split()))
answer = [0 for _ in range(N)]
for i in range(N):
    answer[i] = nums[i]
    for j in range(i):
        if nums[j] < nums[i]:
            answer[i] = max(answer[i],answer[j]+nums[i])
print(max(answer))