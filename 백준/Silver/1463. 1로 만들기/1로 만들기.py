def find_way(num):
    if num == 1:
        return 0
    nums = [0] * (num + 1)

    for i in range(2, num + 1):
        nums[i] = float('inf')

        if i % 3 == 0:
            nums[i] = min(nums[i], nums[i // 3] + 1)

        if i % 2 == 0:
            nums[i] = min(nums[i], nums[i // 2] + 1)

        nums[i] = min(nums[i], nums[i - 1] + 1)

    return nums[num]
print(find_way(int(input())))