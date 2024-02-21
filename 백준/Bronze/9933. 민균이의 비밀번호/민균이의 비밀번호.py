N = int(input())
ss= []
for _ in range(N):
    ss.append(input())
for i in ss:
    to = i[::-1]
    if to == i:
        break
    elif to in ss:
        break
print(len(to),to[len(to)//2])