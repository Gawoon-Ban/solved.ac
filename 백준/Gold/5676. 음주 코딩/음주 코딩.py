import sys

input = sys.stdin.readline

while True:
    try:
        n,k = map(int, input().split())
        # 트리 제작
        tree=[0 for _ in range(n)] + list(map(int, input().split()))
        ans = ""

        for i in range(n,2*n):
            if tree[i] > 0:
                tree[i] = 1
            elif tree[i] < 0:
                tree[i] = -1
            else:
                tree[i] = 0
        for i in range(n-1,0,-1):
            tree[i] = tree[i<<1] * tree[i<<1|1]

        # 쿼리 수행
        for _ in range(k):
            command,l,r =  input().split()

            # 업데이트 수행
            if command == "C":
                p = n + int(l) -1
                if (int(r) > 0) and (tree[p] > 0):
                    continue
                if (int(r) < 0) and (tree[p] < 0):
                    continue
                if (int(r) == 0) and (tree[p] == 0):
                    continue
                if int(r) > 0:
                    tree[p] = 1

                elif int(r) < 0:
                    tree[p] = -1

                else:
                    tree[p]= 0
                while p>1:
                    tree[p>>1] = tree[p] * tree[p^1]
                    p >>= 1
    
            # 출력 수행
            else:
                l = n + int(l) -1
                r = n + int(r) -1
                res = 1
                while l<r:
                    if l&1:
                        res = res * tree[l]
                        l += 1
                    if not(r&1):
                        res = res * tree[r]
                        r -= 1
                    l >>= 1
                    r >>= 1
                    if res == 0:
                        break
                if l == r:
                    res = res * tree[l]
                if res > 0:
                    ans += "+"
                elif res < 0:
                    ans += "-"
                else:
                    ans += "0"
        print(ans)
    except:
        break