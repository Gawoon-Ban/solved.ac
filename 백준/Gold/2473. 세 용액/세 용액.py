import os, io, sys
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
#input = sys.stdin.readline
"""
백준 2473 세 용액

일단 얘는 정렬이 안 되잇네. 
근데 3개를 고르는데 어캐 투 포인터 ㅋㅋ
head고정에 body,tail을 이전과 같이 이동
"""

n = int(input())
arr = list(map(int, input().split()))
arr.sort()
answer = [arr[0], arr[1], arr[2]]
INF = int(1e10)
min_sum = INF
if arr[-1] < 0:
    print(arr[-3], arr[-2], arr[-1])
    sys.exit(0)

for head in range(n-2):
    body = head+1
    tail = n-1
    while body < tail:
        new_sum = arr[head] + arr[body] + arr[tail]
        if abs(new_sum) < min_sum:
            min_sum = abs(new_sum)
            answer = [arr[head], arr[body], arr[tail]]
        if new_sum < 0:
            body += 1
        elif new_sum > 0:
            tail -= 1
        else:
            print(arr[head], arr[body], arr[tail])
            sys.exit(0)
print(*answer)