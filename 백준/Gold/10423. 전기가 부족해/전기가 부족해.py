import sys
input = sys.stdin.readline
from collections import deque
from collections import defaultdict
"""
백준 10423 전기가 부족해

발전소들  -> 모두 0에 연결된 것으로 생각
또한 union할 때 루트 노드가 같으면 빼고
둘의 발전소가 같으면 제외한다.
따라서 루트노드는 기본적으로 큰 아이, BUT 발전소와 연결된 아이이면 발전소로 진행한다.
"""

n,m,k = map(int,input().split())
parent = [i for i in range(n+1)]
power = defaultdict(int)
for i in list(map(int,input().split())):
    power[i] = 1
q = list()
for _ in range(m):
    u,v,w = map(int,input().split())
    q.append((w,u,v))
q.sort()
q =  deque(q)
ans = 0

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x,y):
    r_x = find(x)
    r_y = find(y)
    if r_x == r_y:
        return False
    if r_x in power and r_y not in power:
        parent[r_y] = r_x
    elif r_y in power and r_x not in power:
        parent[r_x] = r_y
    elif r_x in power and r_y in power:
        return False
    else:
        if r_x > r_y:
            parent[r_y] = r_x
        else:
            parent[r_x] = r_y
    return True

while q:
    w,u,v = q.popleft()
    if union(u,v):
        ans += w
print(ans)