import sys

input = sys.stdin.readline

"""
백준 1149 RGB거리

일단 R,G,B의 dp를 각각 한 줄씩 만들어주자. 
이걸 ㅅㅂ 3차원 리스트 이런건 안될거잔아
예를 들어 R의 dp 한 줄은 n번째 집의 색깔을 R로 했을 때, 그때까지 비용의 최솟값인 상황

그렇담 Rdp[new] = min(Gdp[old] + Gcost, Bdp[old] + Bcost) 
"""

N = int(input())
costs = [list(map(int, input().split())) for _ in range(N)]
#순서대로 R,G,B cost

Rdp = [0 for _ in range(N+1)]
Gdp = [0 for _ in range(N+1)]
Bdp = [0 for _ in range(N+1)]

for i in range(1,N+1):
    Rdp[i] = min(Gdp[i-1] + costs[i-1][1], Bdp[i-1]+costs[i-1][2])
    Gdp[i] = min(Rdp[i-1] + costs[i-1][0], Bdp[i-1]+costs[i-1][2])
    Bdp[i] = min(Rdp[i-1] + costs[i-1][0], Gdp[i-1]+costs[i-1][1])
print(min(Rdp[N],Gdp[N],Bdp[N]))