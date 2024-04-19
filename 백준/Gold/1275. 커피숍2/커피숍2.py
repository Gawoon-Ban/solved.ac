import sys

input = sys.stdin.readline

n,q = map(int, input().split())
tree= [0 for _ in range(n)] + list(map(int, input().split()))
for i in range(n-1,0,-1):
    tree[i] = tree[i<<1] + tree[i<<1|1]
for _ in range(q):
    x,y,a,b = map(int, input().split())
    res = 0
    x = x+n-1
    y = y+n-1
    if x>y:
        x,y = y,x
    # 출력 먼저
    while x < y:
        if x&1:
            res += tree[x]
            x += 1
        if not(y&1):
            res += tree[y]
            y -= 1
        x >>= 1
        y >>= 1
    if x == y:
        res += tree[x]
    print(res)

    # 업데이트
    p = a+n-1
    tree[p] = b
    while p>1:
        tree[p>>1] = tree[p] + tree[p^1]
        p >>= 1