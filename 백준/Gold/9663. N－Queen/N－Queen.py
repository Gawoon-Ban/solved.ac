import sys

input = sys.stdin.readline

N = int(input())

pos = [0 for _ in range(N)]

def check(x):
    for i in range(x):
        if pos[x] == pos[i] or abs(pos[x] - pos[i]) == x - i:
            return False
    return True

# cnt는 내가 지금까지 둔 퀸의 개수이자, 지금 둘 퀸의 위치를 나타낸다. 

answer = 0
def dfs(cnt):
    # 그래서 만약 내가 둔 퀸의 개수가 N개면 그 판은 성공한 경우
    if cnt == N:
        global answer
        answer += 1
        return
    else:
        for i in range(N):
            pos[cnt] = i
            if check(cnt):
                dfs(cnt + 1)
dfs(0)
print(answer)    