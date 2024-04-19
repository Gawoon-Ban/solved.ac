import sys

input = sys.stdin.readline
n = int(input())
tree = [0]*(86400*4)
lazy = [0]*(86400*4)

def update_lazy(left,right,node):
    if lazy[node] != 0:
        tree[node] += (right-left+1)*lazy[node]
        if left != right:
            lazy[node*2] += lazy[node]
            lazy[node*2+1] += lazy[node]
        lazy[node] = 0

#left,right: 업데이트 하고자 하는 범위
#start,end: 현재 노드가 담당하는 범위
def update(left,right,start,end,node,diff):
    update_lazy(start,end,node)
    #범위를 벗어난 경우
    if left > end or right < start:
        return
    
    #범위에 쏙 들어가는 경우
    if left <= start and end <= right:
        tree[node] += (end-start+1)*diff
        if start != end:
            lazy[node*2] += diff
            lazy[node*2+1] += diff
        return
    mid = (start+end)//2
    update(left,right,start,mid,node*2,diff)
    update(left,right,mid+1,end,node*2+1,diff)
    tree[node] = tree[node*2] + tree[node*2+1]

for i in range(n):
    a,b,c = input().split()
    start = int(a[0:2])*3600 + int(a[3:5])*60 + int(a[6:8])
    end = int(c[0:2])*3600 + int(c[3:5])*60 + int(c[6:8])
    if start>end:
        update(start,86399,0,86399,1,1)
        update(0,end,0,86399,1,1)
    else:
        update(start,end,0,86399,1,1)

def query(left,right,start,end,node):
    update_lazy(start,end,node)
    if left > end or right < start:
        return 0
    if left <= start and end <= right:
        return tree[node]
    mid = (start+end)//2
    return query(left,right,start,mid,node*2) + query(left,right,mid+1,end,node*2+1)
for _ in range(int(input())):
    a,b,c = input().split()
    start = int(a[0:2])*3600 + int(a[3:5])*60 + int(a[6:8])
    end = int(c[0:2])*3600 + int(c[3:5])*60 + int(c[6:8])
    if start == 0:
        print(query(0,end,0,86399,1)/(end+1))
    elif start>end:
        print((query(start,86399,0,86399,1)+query(0,end,0,86399,1))/(86399-start+1+end+1))
    else:
        print(query(start,end,0,86399,1)/(end-start+1))