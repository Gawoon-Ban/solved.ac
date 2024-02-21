import sys
input = sys.stdin.readline
n = int(input())

cases = {}

def box(num):
    if num in cases:
        return cases[num]

    if num == 1:
        answer= 1
    elif num == 2:
        answer = 2
    else:
        answer = box(num - 1) + box(num - 2)
    
    cases[num] = answer
    return answer

print(box(n)%10007)