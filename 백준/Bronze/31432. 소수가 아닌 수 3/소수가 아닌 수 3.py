import sys
from itertools import product
input = sys.stdin.readline

N = int(input())
ints = list(map(int,input().split()))

def is_prime(n):
    if n == 0 or n == 1:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def all_nums(nums):
    for len_ in range(1,13):
        for comb in product(nums,repeat=len_):
            yield int("".join(map(str,comb)))

for num in all_nums(ints):
    if not is_prime(num):
        print("YES")
        print(num)
        exit()
else:
    print("NO")