def count(n,r,c):
    if n == 1 and r == 0 and c == 0:
        return 0
    elif n==1 and r==0 and c==1:
        return 1
    elif n==1 and r==1 and c==0:
        return 2
    elif n==1 and r==1 and c==1:
        return 3
    elif r<= 2**(n-1)-1 and  c<= 2**(n-1)-1:
        return count(n-1,r,c)
    elif r<= 2**(n-1)-1 and c >2**(n-1)-1:
        return count(n-1,r,c-2**(n-1)) + 2**(2*(n-1))
    elif r> 2**(n-1)-1 and c<= 2**(n-1)-1:
        return count(n-1,r-2**(n-1),c) + 2**(2*n-1)
    else:
        return count(n-1,r-2**(n-1),c-2**(n-1)) + 3*(2**(2*(n-1)))


n,r,c = map(int,input().split())
print(count(n,r,c))