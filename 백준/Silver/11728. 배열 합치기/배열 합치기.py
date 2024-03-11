import sys
input = sys.stdin.readline

n,m = map(int, input().split())

arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
pnt1 = 0
pnt2 = 0
while pnt1<n and pnt2<m:
    if arr1[pnt1] < arr2[pnt2]:
        print(arr1[pnt1], end=' ')
        pnt1 += 1
    else:
        print(arr2[pnt2], end=' ')
        pnt2 += 1
if pnt1 < n:
    for i in range(pnt1, n):
        print(arr1[i], end=' ')
if pnt2 < m:
    for i in range(pnt2, m):
        print(arr2[i], end=' ')