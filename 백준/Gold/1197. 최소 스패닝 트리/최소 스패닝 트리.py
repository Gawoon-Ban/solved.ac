import io,os,sys
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
#input = sys.stdin.readline
write = sys.stdout.write
"""
백준 1197 최소 스패닝 트리

이 문제를 통해 최소 스패닝 트리와 크루스칼 알고리즘을 배워간다
"""

v,e = map(int,input().split())
graph = []
def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]
parent = [i for i in range(v+1)]
for _ in range(e):
    graph.append(list(map(int,input().split())))
graph.sort(key = lambda x : x[2])
answer = 0
cnt = 0
for a,b,c in graph:
    a = find_parent(a)
    b = find_parent(b)
    if a != b:
        parent[b] = a
        answer += c
        cnt += 1
    if cnt == v-1:
        break
write(str(answer))