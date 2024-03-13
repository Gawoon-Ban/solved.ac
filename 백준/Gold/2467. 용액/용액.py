import os, io, sys
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
#input = sys.stdin.readline
"""
백준 2467 용액

일단 오름차순으로 정렬해서 줬고,
투포인터를 쓸건데, 일단 head= 0으로 시작

1. 만약 두 용액이 같은 종류
    이러면 그 중에서 젤 작은거 2개 뽑았을 때가 0에 가장 가까움
    -> 여기서 2개

2. 만약 두 용액이 다른 종류
    head = 0 에서 진행할건데, tail = n-1에서 시작
    tail이 한 칸씩 줄어온다. if abs(이전 합) < abs(현재 합) 이면 현재 head에서는 이 tail이 합쳤을때 0에 제일 가까움
    (head,tail,합)을 저장. head++, tail = n-1로 바꾼 후 다시 돌린다
    하나 걸리는 점은 이분 탐색을 안 씀. 예를 쓸 일이 있나?

    아 설마, 양수와 음수 갈리는 지점을 이거로 찾나?
"""

def binary_search(arr):
    left = 0
    right = len(arr)-1
    while left < right:
        mid = (left+right)//2
        if arr[mid] < 0 and arr[mid+1] > 0:
            return mid
        elif arr[mid] > 0 and arr[mid-1] < 0:
            return mid-1
        elif arr[mid] < 0:
            left = mid+1
        else:
            right = mid-1
    return int(1e9)

n = int(input())
arr = list(map(int, input().split()))
last_minus = binary_search(arr)
if last_minus == int(1e9):
    if arr[0] < 0:
        print(arr[-2], arr[-1])
    else:
        print(arr[0], arr[1])
else:
    head = 0
    tail = n-1
    INF = int(1e10)
    pre_sum = INF
    answers = []
    while head <= last_minus:
        if tail == last_minus:
            answers.append((abs(pre_sum), arr[head], arr[tail+1]))
            head += 1
            tail = n-1
            pre_sum = INF
            continue
        sum_ = arr[head] + arr[tail]
        if abs(sum_) > abs(pre_sum):
            answers.append((abs(pre_sum), arr[head], arr[tail+1]))
            head += 1
            tail = n-1
            pre_sum = INF
            continue
        pre_sum = sum_
        tail -= 1
    if n - last_minus >2:
        answers.append((arr[last_minus+1] + arr[last_minus+2], arr[last_minus+1], arr[last_minus+2]))
    if last_minus >= 2:
        answers.append((abs(arr[last_minus-1] + arr[last_minus]), arr[last_minus-1], arr[last_minus]))
    answers.sort()
    print(answers[0][1], answers[0][2])