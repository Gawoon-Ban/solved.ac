N,M = map(int,input().split())
Dogam = []
Dogam2 = {}
for i in range(N):
    name = input()
    Dogam.append(name)
    Dogam2[name] = i+1

to_answer = []
for _ in range(M):
    to = input()
    to_answer.append(to)

for t in to_answer:
    try:
        a = int(t)
        print(Dogam[a-1])
    except ValueError:
        print(Dogam2[t])