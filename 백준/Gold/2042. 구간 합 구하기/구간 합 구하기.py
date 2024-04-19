import sys

input = sys.stdin.readline

n,m,k = map(int,input().split())

tree = [0 for _ in range(2*n)]
for i in range(n,2*n):
    tree[i] = int(input())
for i in range(n-1,0,-1):
    tree[i] = tree[i<<1] + tree[i<<1|1]
for _ in range(m+k):
    command,a,b = map(int,input().split())

    # 업데이트
    if command == 1:
        p = a+n-1
        tree[p] = b
        while p > 1:
            tree[p>>1] = tree[p] + tree[p^1]
            p >>= 1
    # 출력
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