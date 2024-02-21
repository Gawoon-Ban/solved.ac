import sys
input = sys.stdin.readline

def push_front (dec,x):
    dec.insert(0,x)
    
def push_back (dec,x):
    dec.append(x)
    
def pop_front(dec):
    if len(dec) != 0:
        first = dec.pop(0)
        print(first)
    else:
        print("-1")

def pop_back(dec):
    if len(dec) != 0:
        last = dec.pop(-1)
        print(last)
    else:
        print("-1")

def size (dec):
    print(len(dec))

def empty (dec):
    if len(dec) == 0:
        print("1")
    else:
        print("0")
        
def front (dec):
    if len(dec) != 0:
        print(dec[0])
    else:
        print("-1")
        
def back(dec):
    if len(dec) != 0:
        print(dec[-1])
    else:
        print("-1")
        
num =int(input())
Deque = []
for i in range(num):
    command = input().split()
    
    if command[0] == "push_back":
        push_back(Deque,command[1])
        
    elif command[0] == "push_front":
        push_front(Deque,command[1])
        
    elif command[0] == "pop_front":
        pop_front(Deque)
        
    elif command[0] == "pop_back":
        pop_back(Deque)
        
    elif command[0] == "size":
        size(Deque)
        
    elif command[0] == "empty":
        empty(Deque)
        
    elif command[0] == "front":
        front(Deque)
        
    else:
        back(Deque)