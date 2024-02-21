from collections import Counter
N = int(input())
cards = list(map(int,input().split()))
M = int(input())
target = list(map(int,input().split()))

count = Counter(cards)

for i in target:
    if i in count:
        print(count[i], end = " ")
    else:
        print("0", end = " ")