import math
import sys
input = sys.stdin.readline

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


M, N = map(int, input().split())


for num in range(M, N + 1):
    if is_prime(num):
        print(num)