def divide (size,n):
    if n==1:
        return 0
    
    if size == 5 and n==1:
        return 0
    elif size ==5 and n==2:
        return 1
    elif size == 5 and n==3:
        return 2
    elif size ==5 and n==4:
        return 3
    elif size == 5.0 and n==5.0:
        return 3
    
    if size != 5 and n == size:
        return divide((size-3)/2,(size-3)/2)*2 +1
    elif size != 5 and n>(size//2)+1:
        return divide((size-3)/2,(size-3)/2) + divide((size-3)/2,n-2-(size-3)/2) +1
    elif size != 5 and n==(size//2)+1:
        return divide((size-3)/2,(size-3)/2) +1
    elif size != 5 and n<(size//2)+1:
        return divide((size-3)/2,n-1)
    
n,x = map(int,input().split())
a = 5
for _ in range(n-1):
    a = a*2 +3
print(divide(a,x))