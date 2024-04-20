import sys

input = sys.stdin.readline

n = int(input())
tree = [0 for _ in range(n)] + list(map(int, input().split()))
tree_ind = [0 for _ in range(n)] + [i+1 for i in range(n)]

for i in range(n-1,0,-1):
    if tree[i<<1] > tree[i<<1|1]:
        tree[i] = tree[i<<1|1]
        tree_ind[i] = tree_ind[i<<1|1]
    else:
        tree[i] = tree[i<<1]
        tree_ind[i] = tree_ind[i<<1]
m = int(input())
for _ in range(m):
    command = input().split()
    # 업데이트
    if int(command[0]) == 1:
        p = int(command[1])+n-1
        tree[p] = int(command[2])
        while p>1:
            if tree[p] > tree[p^1]:
                tree[p>>1] = tree[p^1]
                tree_ind[p>>1] = tree_ind[p^1]
            elif tree[p] < tree[p^1]:
                tree[p>>1] = tree[p]
                tree_ind[p>>1] = tree_ind[p]
            else:
                tree[p>>1] = tree[p]
                tree_ind[p>>1] = min(tree_ind[p],tree_ind[p^1])
            p >>= 1

    # 출력
    else:
        res = int(1e10)
        res_ind = 0
        l = n
        r = n+n-1
        while l<r:
            if l&1:
                if res>tree[l]:
                    res = tree[l]
                    res_ind = tree_ind[l]
                elif res == tree[l]:
                    res_ind = min(res_ind,tree_ind[l])
                l += 1
            if not(r&1):
                if res>tree[r]:
                    res = tree[r]
                    res_ind = tree_ind[r]
                elif res == tree[r]:
                    res_ind = min(res_ind,tree_ind[r])
                r -= 1
            l >>= 1
            r >>= 1
        if l == r:
            if res>tree[l]:
                res = tree[l]
                res_ind = tree_ind[l]
            elif res == tree[l]:
                res_ind = min(res_ind,tree_ind[l])
        print(res_ind)