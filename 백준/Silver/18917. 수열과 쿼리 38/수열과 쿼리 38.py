import sys

input = sys.stdin.readline

"""
백준 18917 수열과 쿼리 38 (사실 배경 얻으려고 품 ㅋㅋ)

이건... 뭐 설명이 필요한가
"""
M = int(input())
xor = 0
sum_ = 0
for _ in range(M):
    command = list(map(int, input().split()))
    if command[0] == 1:
        xor ^= command[1]
        sum_ += command[1]   
    elif command[0] == 2:
        xor ^= command[1]
        sum_ -= command[1]
    elif command[0] == 3:
        print(sum_)
    else:
        print(xor)