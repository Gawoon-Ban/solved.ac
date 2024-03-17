import os, io, sys
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
#input = sys.stdin.readline
"""
백준 1717 집합의 표현

그저 분리 집합을 표현하면 되는 문제

find : 부모 찾기
union : 부모 합치기
"""   
def find(x,parent):
    while x != parent[x]:
        x = parent[x]
    return x
def union(x, y,parent):
    par_x = find(x,parent)
    par_y = find(y,parent)
    if par_x != par_y:
        if par_x < par_y:
            parent[par_y] = par_x
        else:
            parent[par_x] = par_y
n, m = map(int, input().split())
parent = [i for i in range(n+1)]
for _ in range(m):
    c, a, b = map(int, input().split())
    if c == 0:
        if a == b:
            continue
        
        union(a, b,parent)
    else:
        if a == b:
            print("YES")
            continue

        if find(a,parent) == find(b,parent):
            print("YES")
        else:
            print("NO")