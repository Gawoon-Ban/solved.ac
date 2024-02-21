import sys
from queue import Queue
input = sys.stdin.readline

n,w,l = map(int,input().split())
trucks = list(map(int,input().split()))
bridge = Queue()
for _ in range(w):
    bridge.put(0)
time = 0
sum =0
while len(trucks) !=0:
    if sum + trucks[0] -bridge.queue[0] <= l:
        sum += trucks[0]
        bridge.put(trucks[0])
        del trucks[0]
        sum -= bridge.queue[0]
        bridge.get()
        time += 1
        
    else:
        bridge.put(0)
        sum -= bridge.queue[0]
        bridge.get()
        time += 1

print(time + w)