import sys


lists = []
for i in range(9):
    integer = int(sys.stdin.readline().strip())
    lists.append(integer)
    
    
max_value = max(lists)
for i in range(9):
    if lists[i] == max_value:
        max_index = i
    

print(max_value)
print(max_index +1)