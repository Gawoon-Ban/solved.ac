import sys
input = sys.stdin.readline

n = int(input())
lines = [list(map(int, input().split()))]
for _ in range(n-1):
    start, end = map(int, input().split())
    for i in range(len(lines)):
        if lines[i][0] <= start <= lines[i][1] or lines[i][0] <= end <= lines[i][1]:
            if lines[i][0] > start:
                lines[i][0] = start
            elif lines[i][1] < end:
                lines[i][1] = end
            break
    else:
        lines.append([start, end])
lines.sort()

result = 0
start, end = lines[0]
for i in range(1, len(lines)):
    if end < lines[i][0]:
        result += end-start
        start, end = lines[i]
    else:
        end = max(end, lines[i][1])
result += end-start

print(result)