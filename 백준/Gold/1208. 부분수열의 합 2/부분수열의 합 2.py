import sys
input = sys.stdin.readline
from itertools import combinations
from collections import Counter 
"""
백준 1208 부분수열의 합 2

Meet in the middle 알고리즘을 처음 배워보는 문제
그냥 브포로 풀려면 최대 2^40으로 시간초과가 난다.
배열 절반 나눔, -> 각각 2^20으로 부분합을 구함
둘다 이중 for문으로 돌리면 똑같이 2^40이 걸리지만, Counter를 사용하여 시간을 줄인다.
원래는 이분탐색을 쓰려고 했으나, COunter의 경우 시간은 덜 걸리면서 중복될 경우까지 잡아준다.
"""

n,s = map(int,input().split())
arr = list(map(int,input().split()))

# 1개일때 예외처리
if n == 1:
    if arr[0] == s:
        print(1)
    else:
        print(0)
    sys.exit(0)

# 배열을 절반 나누고, 부분합을 구한다.
arr1 = arr[:n//2]
arr2 = arr[n//2:]
arr1_sum = []
arr2_sum = []
for i in range(n//2+1):
    for comb in combinations(arr1,i):
        arr1_sum.append(sum(comb))
for i in range(n-n//2+1):
    for comb in combinations(arr2,i):
        arr2_sum.append(sum(comb))

#이분탐색이 아닌, Counter를 사용하여 s-a의 존재여부와 개수를 파악한다. 
arr2_count = Counter(arr2_sum)
ans = 0 
for i in arr1_sum:
    to_find = s-i
    if to_find in arr2_count:
        ans += arr2_count[to_find]

#만약 s==0인 경우 공집합도 넣었으므로 1을 빼준다.
if s == 0:
    ans -= 1
print(ans)