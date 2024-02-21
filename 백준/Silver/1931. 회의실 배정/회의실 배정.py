meetings = []
end_time = 0
answer = 0

n = int(input())
for _ in range(n):
    meetings.append(tuple(map(int,input().split())))

meetings = sorted(meetings, key = lambda x :(x[1],x[0]))
for i in meetings:
    start,end = i
    if start >= end_time:
        answer += 1
        end_time = end
print(answer)