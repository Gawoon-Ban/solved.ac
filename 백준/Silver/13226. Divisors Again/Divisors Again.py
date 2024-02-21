import sys
input = sys.stdin.readline

def count_div(num):
    count = 1 
    i = 2
    while i * i <= num:
        if num % i == 0:
            exponent = 0
            while num % i == 0:
                num //= i
                exponent += 1
            count *= (exponent + 1)
        i += 1

    if num > 1:
        count *= 2  
    return count

line_num = int(input())
for j in range(line_num):
    divisors = []
    L, U = map(int, input().split())
    for k in range(L, U + 1):
        divisors.append(count_div(k))
    print(max(divisors))





