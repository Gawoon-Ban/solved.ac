import sys

input = sys.stdin.readline

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

N = int(input())  
parent = [i for i in range(N + 1)]  

for _ in range(N - 2):  
    a, b = map(int, input().split())  
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

answer = [] 
for i in range(1, N + 1):  
    if i == parent[i]:
        answer.append(i)
print(*answer)