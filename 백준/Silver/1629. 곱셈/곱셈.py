import sys
input = sys.stdin.readline

"""
백준 1629 곱셈 

자 배운걸 써보자고
A^B % C를 구하는 문제인데 이제 A^B를 A^(B/2) 2개로 나눠서 풀어야 한단 말이지. 
아 근데 차피 C로 나눌꺼는 그냥 마지막에서 띡 나누기만 하면 O(1)로 받으니까
A^B를 저거 분할로 구하기만 하면 될듯
"""

def pow(a,b,c):
    if b == 0:
        return 1
    x = pow(a,b//2,c)
    if b % 2 ==0:
        return x*x%c 
    else:
        return x*x*a%c

a,b,c = map(int,input().split())
print(pow(a,b,c))