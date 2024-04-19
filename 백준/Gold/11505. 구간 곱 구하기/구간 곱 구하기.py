import sys

input = sys.stdin.readline

n,m,k = map(int, input().split())
tree = [0 for _ in range(2*n)]

for i in range(n,2*n):
    tree[i] = int(input())%1000000007

for i in range(n-1,0,-1):
    tree[i] = (tree[i<<1] * tree[i<<1|1])%1000000007
for _ in range(m+k):
    a,b,c = map(int,input().split())
    if a == 1:
        p = b+n-1
        tree[p] = c%1000000007
        while p>1:
            tree[p>>1] = (tree[p] * tree[p^1])%1000000007
            p >>= 1
    else:
        res = 1
        l = b+n-1
        r = c+n-1
        while l<r:
            if l&1:
                res = (res*tree[l])%1000000007
                l += 1
            if not(r&1):
                res = (res*tree[r])%1000000007
                r -= 1
            l >>= 1
            r >>= 1
            if res == 0:
                break
        if l == r:
            res = (res*tree[l])%1000000007
        print(res)