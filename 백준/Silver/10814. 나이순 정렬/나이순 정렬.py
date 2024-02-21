import sys


num = int(sys.stdin.readline().strip())
lists = []
for i in range(num):
    age, name = sys.stdin.readline().split()
    person = (int(age), name)
    lists.append(person)
 


answer = sorted(lists, key = lambda x : (x[0]))

for n in answer:
    x,y = n
    print(f"{x} {y}")