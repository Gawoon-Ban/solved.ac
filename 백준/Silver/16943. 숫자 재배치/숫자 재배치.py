import sys
from itertools import permutations
input = sys.stdin.readline
a,b = input().split()
a_= []
for char in a:
    a_.append(char)
a_ = sorted(a_)
ps = list(permutations(a_))
answer = -1
for i in ps:
    if i[0] == '0':
        continue
    if int(''.join(ps[len(ps)-1])) < int(b) and ps[len(ps)-1][0] != '0' :
        answer = ''.join(ps[len(ps)-1])
        print(answer)
        break
    if int(''.join(i)) >= int(b):
        try:
            answer = pre_per
            print(answer)
        except:
            answer = 0
            print("-1")
        break
    pre_per = ''.join(i)
if answer == -1 :
    print("-1")