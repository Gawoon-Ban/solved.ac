import sys
input = sys.stdin.readline

n = int(input())
pair = []
for _ in range(n):
    a, b = map(int, input().split())
    pair.append((a,b))
pair.sort(key=lambda x: (x[0], x[1]))
result = 0
start, end = pair[0]
for i in range(1, len(pair)):
    if end < pair[i][0]:
        result += end-start
        start, end = pair[i]
    else:
        end = max(end, pair[i][1])
result += end-start

print(result)