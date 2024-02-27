import sys
input = sys.stdin.readline

"""
백준 11444 피보나치 수 6
문제: n번째 피보나치 수를 1,000,000,007로 나눈 나머지를 구하라

ㅋㅋ 이거 도른거 같다. 이걸 어캐암 ㅋㅋ
일단 킹무위키 Matrix multiplication 참고해서 해보자고
사실 이거 카테고리에 분할정복을 활용한 거듭제곱이 있잔슴. 근데 피보나치에 거듭제곱이 어딨냐고
그래서 저걸 배열로 만들면 거듭제곱이 사용 가능하다
1 1
1 0 
이 2 by 2 매트릭스를 n-1 번 곱했을때 (0,0)이 fibo n 이다.  
와 근데 백준 numpy도 못 쓰네 ㅋㅋ
이럼 행렬곱도 내가 만들긴 해야함
"""
mat1 = [[1, 1], [1, 0]]

def matmul(mat1_,mat2_):
    a = (mat1_[0][0] * mat2_[0][0] + mat1_[0][1] * mat2_[1][0])%1000000007
    b = (mat1_[0][0] * mat2_[0][1] + mat1_[0][1] * mat2_[1][1])%1000000007
    c = (mat1_[1][0] * mat2_[0][0] + mat1_[1][1] * mat2_[1][0])%1000000007
    d = (mat1_[1][0] * mat2_[0][1] + mat1_[1][1] * mat2_[1][1])%1000000007
    return_mat = [[a, b], [c, d]]   
    return return_mat

def matpow(a,b):
    # n은 행렬이 n승이라는 의미다
    if b==1:
        return a 
    x = matpow(a,b//2)
    y = matmul(x,x)
    if b%2 == 0:
        return y
    else:
        return matmul(y,a)

N = int(input())
if N ==0:
    print(0)
elif N == 1:
    print(1)
else:
    print(matpow(mat1,N-1)[0][0])