import sys
input = sys.stdin.readline

n = int(input())
pair = []
for _ in range(n):
    a, b = map(int, input().split())
    pair.append([a,b])
pair.sort(key=lambda x: (x[0], x[1]))
ind = 0
next = 1
ans = 0
while (ind <= n-1) and (next <= n-1):
    # 안 겹칠 때:
    if pair[ind][1] < pair[next][0]:
        ans += pair[ind][1] - pair[ind][0]
        ind = next
        next += 1
    # 겹칠 때:
    else:
        # 다음 선분이 포함될 때:
        if pair[ind][1] > pair[next][1]:
            next += 1

        # 다음 선분이 더 길 때 or 끝이 같을 때:
        else:
            ans += pair[next][0] - pair[ind][0]
            ind = next
            next += 1
print(ans+pair[ind][1]-pair[ind][0])