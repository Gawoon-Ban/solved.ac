import os, io, sys
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
#input = sys.stdin.readline
"""
백준 1806 부분합

포인터 2개를 둘다 0으로 두고, 만약 사이 sum이 S보다 작으면 tail++
크면 head++ 이때의 길이를 저장, 최소길이 갱신
"""
n,s = map(int, input().split())
arr = list(map(int, input().split()))
INF = int(1e9)
head, tail = 0, 0
answer = INF
sum = arr[0]
for i in arr:
    if i >= s:
        print(1)
        sys.exit(0)
while True:
    if sum >= s:
        answer = min(answer,tail-head+1)
        sum -= arr[head]
        head += 1
    elif tail == n-1:
        break
    else:
        tail += 1
        sum += arr[tail]

if answer == INF:
    print(0)
else:
    print(answer)