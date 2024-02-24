import sys
input = sys.stdin.readline
N,K = map(int, input().split())
q = [N]
value = [0 for _ in range(100002)]
while q:
    x = q.pop(0)
    if x == K:
        print(value[x])
        break
    if x > 100000 or x<0:
        continue
    if x+1 < 100002:
        if value[x+1] == 0:
            value[x+1] = value[x]+1
            q.append(x+1)
    if x>=1:
        if value[x-1] == 0:
            q.append(x-1)
            value[x-1] = value[x]+1
    if x*2 < 100002:
        if value[x*2] == 0:
            q.append(x*2)
            value[x*2] = value[x]+1