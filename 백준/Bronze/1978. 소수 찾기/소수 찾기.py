import math
import sys
input = sys.stdin.readline

def is_prime(num_):
    if num_ < 2:
        return False
    for i in range(2, int(math.sqrt(num_)) + 1):
        if num_ % i == 0:
            return False
    return True


num = int(input())
nums = input().split()
count = 0
for i in range(num):
    if is_prime(int(nums[i])):
        count += 1
        
print(count)