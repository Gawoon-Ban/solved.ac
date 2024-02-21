import sys
input = sys.stdin.readline
def put_x (heap,x):
    if len(heap)==0 or len(heap)==1:
        heap = [0,x]
        return heap
    heap.append(x)
    position = len(heap) -1

    while position >0:
        parent_index = (position)//2
        if heap[parent_index] > heap[position]:
           heap[parent_index], heap[position] = x, heap[parent_index]
           position = parent_index
        else:
            break
    return heap

def print_min(heap):
    if len(heap) ==0 or len(heap) == 1:
        print("0")
        return heap

    min = heap[1]
    print(min)
    heap[1] = heap[len(heap)-1]
    heap.pop(len(heap)-1)
    position = 1
    while True:
        left = 2*position
        right = left +1
        if right <= len(heap)-1 and heap[left] > heap[right]:
            left = right
        if left <= len(heap)-1 and heap[left] < heap[position]:
            heap[left], heap[position] = heap[position], heap[left]
            position = left
        else:
            break
    return heap


heap = []

n = int(input())
for _ in range(n):
    command = int(input())
    if command == 0:
        heap = print_min(heap)
    else:
        heap = put_x(heap,command)
