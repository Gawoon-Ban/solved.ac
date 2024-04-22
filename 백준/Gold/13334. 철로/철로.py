import sys
input = sys.stdin.readline
import heapq

n = int(input())
lines = []
for _ in range(n):
    a,b = map(int, input().split())
    lines.append((min(a,b),max(a,b)))
lines.sort(key = lambda x:(x[1],x[0]))
heap = []
d = int(input())
ans = 0
for start,end in lines:
    if end-start > d:
        continue
    heapq.heappush(heap, start)
    while True:
        if heap[0] < end-d:
            heapq.heappop(heap)
        else:
            break
    ans = max(ans, len(heap))
print(ans)