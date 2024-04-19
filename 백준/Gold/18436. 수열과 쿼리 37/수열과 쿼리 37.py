import sys

input = sys.stdin.readline

n = int(input())

# tree의 각 항은 홀수의 개수를 나타낸다. 
tree = [0 for _ in range(n)] + list(map(int, input().split()))

for i in range(n,2*n):
    if tree[i]%2 == 0:
        tree[i] = 0
    else:
        tree[i] = 1
for i in range(n-1,0,-1):
    tree[i] = tree[i*2] + tree[i*2+1]

for _ in range(int(input())):
    command,a,b = map(int, input().split())
    if command == 1:
        p = n+a-1
        tree[p] = b%2
        while p>1:
            tree[p>>1] = tree[p] + tree[p^1]
            p >>= 1
    elif command == 2:
        l = a+n-1
        r = b+n-1
        res = r-l+1
        while l<r:
            if l&1:
                res -= tree[l]
                l += 1
            if not(r&1):
                res -= tree[r]
                r -= 1
            l >>= 1
            r >>= 1
        if l == r:
            res -= tree[l]
        print(res)
    else:
        l = a+n-1
        r = b+n-1
        res = 0
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