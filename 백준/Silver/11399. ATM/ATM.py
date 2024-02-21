people_num = int(input())
times = map(int,input().split())
times = sorted(times)
rate = [k for k in range(people_num,0,-1)]
sum = 0 

for j in range(people_num-1,-1,-1):
    time = times[j] * rate[j]
    sum += time

print(sum)