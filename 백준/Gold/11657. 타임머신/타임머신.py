import sys
input = sys.stdin.readline

"""
백준 11657 타임머신
일단 얘는 벨만포드 익숙해지려고 클4 문제 풀기 전에 풀어보는
일단 문제의 출력 조건을 보면, 무한히 예전으로 돌린다는 거는 음수 순환을 의미하는거 같음
그럼 bf 끝나고 마지막에 한번 더 돌려서 음수인지 확인해보면 될거고,
그거랑 INF 일때 -1 출력하는거 말고는 그냥 벨포인듯?
"""

INF = int(1e9)
N,M = map(int,input().split())
graph = []
distance = [INF] * (N+1)
for _ in range(M):
    a,b,c = map(int,input().split())
    graph.append((a,b,c))
start = 1
def bf(start):
    distance[start] = 0
    for _ in range(N-1):
        for i in range(M):
            st_pos,end_pos,w = graph[i]
            if distance[st_pos] != INF and distance[end_pos] > distance[st_pos] + w:
                distance[end_pos] = distance[st_pos] + w
    for i in range(M):
        st_pos,end_pos,w = graph[i]
        if distance[st_pos] != INF and distance[end_pos] > distance[st_pos] + w:
            return False
    return True

if bf(1):
    for i in range(2,N+1):
        if distance[i] == INF:
            print(-1)
        else:
            print(distance[i])
else:
    print(-1)