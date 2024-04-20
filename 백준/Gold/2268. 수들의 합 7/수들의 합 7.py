import sys

input = sys.stdin.readline

n,m = map(int, input().split())
tree = [0 for _ in range(2*n)]

for _ in range(m):
    command,a,b= map(int, input().split())
    
    # sum
    if command == 0:
        l = a+n-1
        r = b+n-1
        if r<l:
            l,r = r,l
        res = 0
        while l<r:
            if l%2:
                res += tree[l]
                l += 1
            if not(r%2):
                res += tree[r]
                r -= 1
            l //= 2
            r //= 2
        if l == r:
            res += tree[l]
        print(res)
    # update
    else:
        p = a+n-1
        tree[p] = b
        while p>1:
            tree[p>>1] = tree[p] + tree[p^1]
            p >>= 1