import os, io, sys
from bisect import bisect_left
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
#input = sys.stdin.readline
"""
백준 2550 전구

일단 그림부터 바로 전에 풀었던 꼬인 전깃줄과 비슷함
가장 많은 전구가 켜지도록 -> Lis
하지만 얘는 Lis의 값을 정확히 구해야 하기에 record 사용
"""
n = int(input())
switch = list(map(int, input().split()))
light = list(map(int, input().split()))
switch_idx = [0] * (n)
for i in range(n):
    for j in range(n):
        if light[j] == switch[i]:
            switch_idx[i] = j
            break
record = [0] * (n)
Lis = [switch_idx[0]]

for i in range(1,n):
    if switch_idx[i] > Lis[-1]:
        Lis.append(switch_idx[i])
        record[i] = len(Lis)-1
    else:
        idx = bisect_left(Lis,switch_idx[i])
        Lis[idx] = (switch_idx[i])
        record[i] = idx

a = len(Lis)-1
ans = []
for i in range(n-1,-1,-1):
    if record[i] == a:
        ans.append(switch[i])
        a -= 1
ans.sort()
print(len(ans))
print(*ans)