import sys
input = sys.stdin.readline

N = int(input())
if N == 0:
    print("NO")
else:
    fac = 1
    facs = [1]
    mul = 1
    while fac <= N:
        fac *= mul
        facs.append(fac)
        mul += 1
    max_fac = mul - 2
    facs.pop(-1)
    sums = []
    for i in range(1,(1 << max_fac+1)):
        sum = 0
        for j in range(max_fac+1):
            if i & (1<<j):
                sum += facs[j]
        sums.append(sum)
    if N in sums:
        print("YES")
    else:
        print("NO")