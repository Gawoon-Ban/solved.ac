import sys

input = sys.stdin.readline


n,m = map(int, input().split())
inf = int(1e10)
min_tree = [inf for _ in range(2*n)]

# 트리 제작
for i in range(n):
    x = int(input())
    min_tree[n+i] = x
for i in range(n-1,0,-1):
    min_tree[i] = min(min_tree[i<<1],min_tree[i<<1|1])

# 쿼리 수행
for _ in range(m):
    l,r = map(int, input().split())

    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!1
    # 이렇게 n을 더한 후 , 1을 빼주어야 한다.
    l += n
    l -= 1
    r += n
    r -= 1
    min_res = inf
    while l<r:
        if l&1:
            min_res = min(min_res,min_tree[l])
            l += 1
        if not(r&1):
            min_res = min(min_res,min_tree[r])
            r -= 1
        l >>= 1
        r >>= 1
    
    if l == r:
        min_res = min(min_res,min_tree[l])
    
    print(min_res)