listen_num , see_num = map(int,input().split())
listen = []
see = []
for i in range(listen_num):
    name = input()
    listen.append(name)
for j in range(see_num):
    name = input()
    see.append(name)
listen = set(listen)
see = set(see)

answer = listen.intersection(see)
answer = list(answer)
answer.sort()
print(len(answer))
for t in answer:
    print(t)