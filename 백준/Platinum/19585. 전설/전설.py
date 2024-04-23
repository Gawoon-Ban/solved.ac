import sys

input = sys.stdin.readline

c,n= map(int,input().split())   

# key가 없을 때는 검색하면 안되니 default dict가 아닌 기본 dict를 사용한다.

colors = {}
for _ in range(c):
    pos = colors
    for i in input().rstrip():

        # 새로운 key일 때 -> 새 노드를 만들어준다. 
        if not(pos.get(i)):
            pos[i] = {}

        # 자식 노드로 이동한다.
        pos = pos[i]
    
    # 0 즉, 리프노드임을 표시한다.
    pos[0] = 1

names = {input().rstrip() for _ in range(n)}

def trie(string):
    # 루트노드 시작
    pos = colors

    for i in range(len(string)):

        # 리프노드 도착 (즉, color가 존재) + color 뒤에 있는 str이 names에 있을 때
        if pos.get(0) and string[i:] in names:
            return 1
        
        # 해당 노드가 없을 때, 즉 color가 아닐때
        if not(pos.get(string[i])):
            return 0
        
        # 자식 노드로 이동
        pos = pos[string[i]]

for _ in range(int(input())):
    print("Yes" if trie(input().rstrip()) else "No")