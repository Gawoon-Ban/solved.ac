import sys
input = sys.stdin.readline

num = int(input())
lists = []
for i in range(num):
    coordinate = input().split()
    coordinate[0] = int(coordinate[0])
    coordinate[1] = int(coordinate[1])
    lists.append(coordinate)
 




answer = sorted(lists, key = lambda x : (x[0],x[1]))

for n in answer:
    x,y = n
    print(f"{x} {y}")