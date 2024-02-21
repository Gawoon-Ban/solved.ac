import sys
input = sys.stdin.readline

def is_triangle (list_):
    largest = max(list_)
    list_.remove(largest)
    a = list_[0]
    b = list_[1]
    if largest**2 == a**2 + b**2:
        return "right"
    else:
        return "wrong"
    
results =[]

while True:
    triangle = list(map(int,input().split()))
    if triangle[0] == 0 and triangle[1] == 0 and triangle[2] == 0:
        break
    else:
        results.append(is_triangle(triangle))
        
for i in results:
    print(i)