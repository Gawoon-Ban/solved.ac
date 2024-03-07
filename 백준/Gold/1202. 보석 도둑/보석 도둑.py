import io,os,sys
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
#input = sys.stdin.readline

"""
백준 1202 보석 도둑

일단 가방 하나에 하나의 보석만 담을 수 있다는 것이 중요하다.
heapq를 사용하여 최대 순서로 저장하고.
가방을 sort
이중 for문으로 가방에 보석 담기
근데 사실 이럴거였으면 heqpq를 쓸 필요 없음 - > O(N^2)

이제 슬슬 시간복잡도 계산해가면서 얘가 될지 확인 해보자
"""

import heapq
n,k = map(int,input().split())
jewels = []
bags = []
for _ in range(n):
    heapq.heappush(jewels,list(map(int,input().split())))
for _ in range(k):
    bags.append(int(input()))
bags.sort()
answer = 0
jew_in_bag = []
for bag in bags:
    while jewels and bag >= jewels[0][0]:
        weight, value = heapq.heappop(jewels)
        heapq.heappush(jew_in_bag,(-value,weight))
    if jew_in_bag:
        answer -= heapq.heappop(jew_in_bag)[0]
print(answer)