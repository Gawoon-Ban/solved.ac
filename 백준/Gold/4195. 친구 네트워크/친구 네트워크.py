#import os, io, sys
import sys
#input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
input = sys.stdin.readline
#print = sys.stdout.write
"""
백준 4195 친구 네트워크

애도 분리집합만 쓰면 문제가 없어 보인다.
다만 이름이 int가 아닌 string이므로 dict 사용
이 dict에는 각 노드의 부모 노드가 들어갈 것인데, 이때 사전순으로 정렬
또한 dict에 현재 그거와 연결된 넥 수 표시
""" 
def find(x):
    while x != f_net[x][0]:
        x = f_net[x][0]
    return x
def union(x, y):
    par_x = find(x)
    par_y = find(y)
    if par_x != par_y:
        cur_num = f_net[par_x][1] + f_net[par_y][1]
        f_net[par_x][1] = cur_num
        f_net[par_y]= [par_x,cur_num]
        f_net[x] = [par_x, cur_num]
        f_net[y] = [par_x, cur_num]
        answers.append(cur_num)
    else:
        answers.append(f_net[par_x][1])
        f_net[x] = [par_x, f_net[par_x][1]]
        f_net[y] = [par_x, f_net[par_x][1]]
answers = []
for _ in range(int(input())):
    f_net = {}
    f = int(input())
    for __ in range(f):
        a, b = input().split()
        if a not in f_net:
            f_net[a] = [a,1]
        if b not in f_net:
            f_net[b] = [b,1]
        union(a, b)
        
for ans in answers:
    print(ans)