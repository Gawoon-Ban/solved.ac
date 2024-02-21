import sys
input = sys.stdin.readline

queue = []
common_num = int(input())
count = 0
while count < common_num:
    common = input().split()
    if common[0] == "push":
        
        num = int(common[1])
        queue.append(num)
      
    
    elif common[0] == "pop":
        if len(queue) == 0:
            print("-1")
        else:
            print(queue.pop(0))
            
        
    elif common[0] == "size":
        print(len(queue))
        
    elif common[0] == "empty":
        if len(queue) == 0:
            print("1")
        else :
            print("0")
            
    elif common[0] == "front":
        if len(queue) == 0:
            print("-1")
        else:
            print(queue[0])
            
    else:
        if len(queue) == 0:
            print("-1")
        else:
            print(queue[-1])
            
    count += 1
        