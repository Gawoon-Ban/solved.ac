import sys
input = sys.stdin.readline

n,m = map(int,input().split())
tree = [0 for _ in range(2*n)]
ans = 0
query = [[]for _ in range(n+1)]
for _ in range(m):
    a,b = map(int,input().split())
    query[a].append(b)
for i in range(n+1):
    query[i].sort() 
for q in query:
    if not q:
        continue
    for j in q:
        l = j+n
        p =j+n-1
        tree[p] += 1
        while p > 1:
            tree[p>>1] = tree[p] + tree[p^1]
            p >>= 1
        r = n+n-1
        while l < r:
            if l&1:
                ans += tree[l]
                l += 1
            if not(r&1):
                ans += tree[r]
                r -= 1
            l >>= 1
            r >>= 1
        if l == r:
            ans += tree[l]
print(ans)