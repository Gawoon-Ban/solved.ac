import sys

input = sys.stdin.readline

n = int(input())
tree = [0 for _ in range(n)] + list(map(int, input().split()))

for i in range(n-1,0,-1):
    tree[i] = min(tree[i<<1],tree[i<<1|1])

m = int(input())
for _ in range(m):
    command,a,b = map(int, input().split())
    if command == 1:
        p = a+n-1
        tree[p] = b
        while p > 1:
            tree[p>>1] = min(tree[p],tree[p^1])
            p >>= 1
    else:
        res = int(1e10)
        l = a+n-1
        r = b+n-1
        while l<r:
            if l&1:
                res = min(res,tree[l])
                l += 1
            if not(r&1):
                res = min(res,tree[r])
                r -= 1
            if res == 1:
                break
            l >>= 1
            r >>= 1
        if l == r:
            res = min(res,tree[l])
        print(res)