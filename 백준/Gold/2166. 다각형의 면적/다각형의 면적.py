import io,os,sys
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
#input = sys.stdin.readline

"""
백준 2166 다각형의 면적

아 신발끈 공식 ㅋㅋ
"""

n = int(input())
pots = [list(map(int, input().split())) for _ in range(n)]
first_sum = 0
second_sum = 0
for i in range(n-1):
    # x1 * y2 + x2 * y3 + ... 
    first_sum += pots[i][0] * pots[i+1][1]
    # y1 * x2 + y2 * x3 + ... + yn * x1
    second_sum += pots[i][1] * pots[i+1][0]
# + xn * y1
first_sum += pots[n-1][0] * pots[0][1]
# + yn * x1
second_sum += pots[n-1][1] * pots[0][0]
print(round(abs(first_sum-second_sum)/2,2))