import sys
from collections import deque
input = sys.stdin.readline

LOG = 17
n = int(input().rstrip())
graph = [[] for _ in range(n+1)]

# 첫째항은 부모, 둘째 항은 부모까지 거리
tree = [[[0,0] for _ in range(LOG)] for _ in range(n+1)]

d = [-1 for _ in range(n+1)]

for _ in range(n-1):
    a,b,w = map(int, input().rstrip().split())
    graph[a].append((b,w))
    graph[b].append((a,w))

# 항상 있는 1을 루트노드로 트리 생성
# 이때 노드들의 depth를 저장하며, 부모 노드와 거리를 저장한다.
q = deque([1])
d[1] = 0
tree[1][0][0] = 1
tree[1][0][1] = 0
while q:
    pos = q.popleft()
    for next, w in graph[pos]:
        if tree[next][0][0] == 0:
          tree[next][0][0] = pos
          tree[next][0][1] = w
          d[next] = d[pos] + 1
          q.append(next)


# 2^k 번째 조상과 거리를 저장
for i in range(1,LOG):
    for j in range(1,n+1):
        tree[j][i][0] = tree[tree[j][i-1][0]][i-1][0]
        tree[j][i][1] = tree[j][i-1][1] + tree[tree[j][i-1][0]][i-1][1]


for _ in range(int(input().rstrip())):
    a,b = map(int, input().rstrip().split())
    ans = 0

    # 더 깊은 애를 b로
    if d[a] > d[b]:
        a,b = b,a

    # 먼저 둘의 레벨을 같게
    for i in range(LOG-1,-1,-1):
        if d[b] - d[a] >= (1 << i):
            ans += tree[b][i][1]
            b = tree[b][i][0]
    
    # 만약 이거로 레벨이 같아진다면
    if a == b:
        print(ans)
        continue

    # 둘의 부모가 같아질때까지
    for i in range(LOG-1,-1,-1):
        if tree[a][i][0] != tree[b][i][0]:
            ans += tree[a][i][1] + tree[b][i][1]
            a = tree[a][i][0]
            b = tree[b][i][0]
    
    # 이제 조상이 같아졌기에 한번 더 이동
    ans += tree[a][0][1] + tree[b][0][1]
    print(ans)