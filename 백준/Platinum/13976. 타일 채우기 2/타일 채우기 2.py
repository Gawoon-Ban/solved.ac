import sys
input = sys.stdin.readline  

n = int(input())


def matmul(a,b):
    res = [[0,0],[0,0]]
    res[0][0] = (a[0][0]*b[0][0] + a[0][1]*b[1][0])%1000000007
    res[0][1] = (a[0][0]*b[0][1] + a[0][1]*b[1][1])%1000000007
    res[1][0] = (a[1][0]*b[0][0] + a[1][1]*b[1][0])%1000000007
    res[1][1] = (a[1][0]*b[0][1] + a[1][1]*b[1][1])%1000000007
    return res


def expo(a,b):
    if b == 0:
        return [[1,0],[0,1]]
    if b == 1:
        return a
    x = expo(a,b//2)
    if b % 2 == 0:
        return  matmul(x,x)
    else:
        return matmul(matmul(x,x),a)
if n%2 == 1:
    print(0)
    sys.exit(0)

x = expo([[4,-1],[1,0]],n//2-1)
print((x[0][0]*3 + x[0][1])%1000000007)