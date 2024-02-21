nums={}
def fibo (N):
    if N in nums:
        return nums[N]

    if N==0:
        answer = [1,0]
    elif N == 1:
        answer = [0,1]
    else:
        answer = [fibo(N-1)[0]+fibo(N-2)[0],fibo(N-1)[1]+fibo(N-2)[1]]

    nums[N] = answer
    return answer

Nums = int(input())

for _ in range(Nums):
    a,b = (fibo(int(input())))
    print(f"{a} {b}")