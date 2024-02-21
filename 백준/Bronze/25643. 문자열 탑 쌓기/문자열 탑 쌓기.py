import sys
def compare_str (str1,str2,M):
    for i in range(M):
        if str1[M-1-i:] == str2[:i+1]:
            return True
    for i in range(M):
        if str2[M-1-i:] == str1[:i+1]:
            return True
    return False
N,M = map(int,sys.stdin.readline().strip("\n").split())
strs =[]
for _ in range(N):
    str = sys.stdin.readline().strip("\n")
    strs.append(str)
if N == 1:
    print(1)
else:
    is_same = False
    for j in range(N-1):
        if compare_str(strs[j],strs[j+1],M):
            is_same = True
        else:
            is_same = False
            break
    if is_same:
        print(1)
    else:
        print(0)