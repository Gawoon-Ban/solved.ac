import sys
input = sys.stdin.readline

num = int(input())
score = input().split()
for i in range(num):
    score[i] = int(score[i])

sum = 0
max_value = max(score)
for i in range(num):
    score[i] = score[i]/max_value *100
   
    
for i in score:
    sum +=  i
    
print(sum/num)