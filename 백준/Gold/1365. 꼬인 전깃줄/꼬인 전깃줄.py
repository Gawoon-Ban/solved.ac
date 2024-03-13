import os, io, sys
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
#input = sys.stdin.readline
"""
백준 1365 꼬인 전깃줄

꼬이지 않는 다는 것이 어떤 의미일까? 
예시의 1과 같이 역전하는 것이 없다는 것 -> 걍 Lis 찾으라는 거임
ans = n - len(Lis)
"""
n = int(input())
arr = list(map(int, input().split()))
Lis = [arr[0]]
def b_s (lis,target):
    s,e=  0,len(lis)-1
    while s<e:
        mid = (s+e)//2
        if lis[mid] < target:
            s = mid + 1
        elif lis[mid] == target:
            return mid
        elif lis[mid-1] < target < lis[mid]:
            return mid
        else:
            e = mid
    return e
for i in arr:
    if i > Lis[-1]:
        Lis.append(i)
    else:
        idx = b_s(Lis,i)
        Lis[idx] = i
print(n-len(Lis))