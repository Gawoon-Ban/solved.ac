import sys
input = sys.stdin.readline
from bisect import bisect_left
"""
백준 12015 가장 긴 증가하는 부분 수열 2

전형적인 Lis 문제, BUT input의 크기와 시간이 심상치 않다.
이진탐색을 이용하여 Lis를 O(nlogn)으로 푸는 방법을 익히기 위한 문제
"""
n = int(input())
arr = list(map(int, input().split()))
Lis = []
Lis.append(arr[0])
for i in range(1,n):
    if arr[i] > Lis[-1]:
        Lis.append(arr[i])
    else:
        idx = bisect_left(Lis, arr[i])
        Lis[idx] = arr[i]
print(len(Lis)) 