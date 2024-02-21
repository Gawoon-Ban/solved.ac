N,K = map(int,input().split())


nums = [i for i in range(1,N+1)]

answer = []
position = 0
while len(nums) != 0 :
   position = (position + K -1) % len(nums)
   people = nums.pop(position)
   answer.append(people)

for t in answer:
   if len(answer) == 1:
      print(f"<{t}>")
      break
   if t == answer[0]:
      print(f"<{t}", end=", ")
   elif t == answer[N-1]:
      print(f"{t}>")
   else:
      print(t, end=", ")