import sys

input = sys.stdin.readline

n,q = map(int, input().split())
tree = [0 for _ in range(2*n)]

for _ in range(q):
    a,b,c = map(int,input().split())
    if a == 1:
        p = b+n-1
        tree[p] += c
        while p>1:
            tree[p>>1] = tree[p] + tree[p^1]
            p >>= 1
    else:
        res = 0
        l = b+n-1
        r = c+n-1
        while l<r:
            if l&1:
                res += tree[l]
                l += 1
            if not(r&1):
                res += tree[r]
                r -= 1
            l >>= 1
            r >>= 1
        if l == r:
            res += tree[l]
        print(res)