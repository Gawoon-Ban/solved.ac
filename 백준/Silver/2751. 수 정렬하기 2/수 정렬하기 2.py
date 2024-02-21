import sys
input = sys.stdin.readline

num =int(input())
nums =[]
for i in range(num):
    number = int(input())
    nums.append(number)
    
nums.sort()

for i in nums:
    print(i)