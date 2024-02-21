import sys
input = sys.stdin.readline

def GCD(num1, num2):
    max_ = max(num1, num2)
    for i in range(max_,0,-1):
        if num1 % i == 0 and num2 % i == 0:
            return i

def LCM(num1, num2):
    min_ = min(num1,num2)
    while True:
        if min_ % num1 == 0 and min_ % num2 == 0:
            return min_
        min_ += 1
        
num1_,num2_ = map(int,input().split())
print(GCD(num1_,num2_))
print(LCM(num1_,num2_))