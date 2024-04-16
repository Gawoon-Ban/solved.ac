import sys
input = sys.stdin.readline

def solve(start):
    for i in range(start,N+1):

        # a 점화식
        a[i] = min(b[i-1]+1,c[i-1]+1)
        if (line1[i-1] + line2[i-1]) <= W:
            a[i] = min(a[i],a[i-1]+1)
        if i > 1:
            if ((line1[i-2] + line1[i-1]) <= W) and ((line2[i-2] + line2[i-1]) <= W):
                a[i] = min(a[i],a[i-2]+2)


        if i == N:
            return (a[N],b[N-1],c[N-1],a[N-1])
        
        # b 점화식
        b[i] = a[i] + 1
        if (line1[i-1] + line1[i]) <= W:
            b[i] = min(b[i],c[i-1]+1)
        
        # c 점화식
        c[i] = a[i] + 1
        if (line2[i-1] + line2[i]) <= W:
            c[i] = min(c[i],b[i-1]+1)


for _ in range(int(input())):
    N,W = map(int,input().split())
    line1 = list(map(int,input().split()))
    line2 = list(map(int,input().split()))

    # N이 1일 때 예외처리
    if N == 1:
        if (line1[0] + line2[0]) <= W:
            print(1)
        else:
            print(2)
        continue
    
    # 0과 N-1에 걸치는 경우가 없는 경우

    a = [0]*(N+1)
    b = [0]*(N+1)
    c = [0]*(N+1)

    b[0] = 1
    c[0] = 1

    answer = solve(1)[0]

    # 1번 라인에서 0,N-1 라인이 겹치는 경우
    if (line1[0] + line1[N-1]) <= W:

        a[1] = 1
        b[1] = 2
        if (line2[0] + line2[1]) <= W:
            c[1] = 1
        else:
            c[1] = 2

        answer = min(answer, solve(2)[2] + 1)

    # 2번 라인에서 0,N-1 라인이 겹치는 경우
    if (line2[0] + line2[N-1]) <= W:

        a[1] = 1
        c[1] = 2
        if (line1[0] + line1[1]) <= W:
            b[1] = 1
        else:
            b[1] = 2
        
        answer = min(answer, solve(2)[1] + 1)

    # 두 라인 모두에서 겹칠 때
    if ((line1[0] + line1[N-1]) <= W) and ((line2[0] + line2[N-1]) <= W):
        a[1] = 0
        b[1] = 1
        c[1] = 1

        answer = min(answer, solve(2)[3]+2)
    print(answer)