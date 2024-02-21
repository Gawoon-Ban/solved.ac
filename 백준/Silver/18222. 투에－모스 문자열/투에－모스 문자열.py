import sys
def fine_max(k):
    num = 1
    count = 0
    while num <= k:
        num *= 2
        count +=1
    return count-1

k = int(sys.stdin.readline())

count_ =0
mill = 0
if k == 1:
    print(0)
    mill = 1
while k !=1:
    max_num = fine_max(k)
    if 2**max_num == k:
        if max_num%2 + count_%2==0:
            print(0)
            mill = 1
            break
        elif max_num%2 + count_%2 ==1:
            print(1)
            mill = 1
            break
        else:
            print(0)
            mill = 1
            break
    else:
        k = k- 2**max_num
        count_ +=1
if count_%2 == 1 and mill ==0:
    print(1)
elif count_%2 ==0 and mill == 0:
    print(0)