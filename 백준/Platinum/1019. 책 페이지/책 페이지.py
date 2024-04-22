import sys
input = sys.stdin.readline

str_n = input().rstrip()
length = len(str_n)
int_n = int(str_n)

ans = [0 for _ in range(10)]
if length == 1:
    if int_n == 1:
        print("0 1 0 0 0 0 0 0 0 0")
    elif int_n == 2:
        print("0 1 1 0 0 0 0 0 0 0")
    elif int_n == 3:
        print("0 1 1 1 0 0 0 0 0 0")
    elif int_n == 4:
        print("0 1 1 1 1 0 0 0 0 0")
    elif int_n == 5:
        print("0 1 1 1 1 1 0 0 0 0")
    elif int_n == 6:
        print("0 1 1 1 1 1 1 0 0 0")
    elif int_n == 7:
        print("0 1 1 1 1 1 1 1 0 0")
    elif int_n == 8:
        print("0 1 1 1 1 1 1 1 1 0")
    elif int_n == 9:
        print("0 1 1 1 1 1 1 1 1 1")
    sys.exit(0)
for i in range(length-1,-1,-1):
    #일의 자리수부터 진행한다.

    # 즉 현재 살펴보는 자릿수가 일의 자리일 때
    if i == (length-1):
        for j in range(10):
            if j == 0:
                ans[0] += int(str_n[:i])
            elif j<= int(str_n[i]):
                ans[j] = int(str_n[:i]) + 1
            else:
                ans[j] = int(str_n[:i])
    
    # 현재 살펴보는 자릿수가 가장 큰 자릿수 일 때
    elif i == 0:
        for j in range(1,10):
            if j< int(str_n[0]):
                ans[j] += 10**(length-1)
            elif j == int(str_n[0]):
                ans[j] += int(str_n[1:])+1
    
    else:
        for j in range(10):
            if j == 0:
                if int(str_n[i]) ==0:
                    minimum = int("1"+ "0"*(length-i-1))
                    maximum = int(str_n[:i] + str_n[i+1:])
                    ans[0] += maximum-minimum+1
                else:
                    ans[0] += int(str(int(str_n[:i])+1)+"0"*(length-i-1))-1-int("1"+ "0"*(length-i-1))+1
            elif j< int(str_n[i]):
                ans[j] += int(str(int(str_n[:i])+1)+"0"*(length-i-1))
            elif j == int(str_n[i]):
                ans[j] += int(str_n[:i]+str_n[i+1:])+1
            else:
                ans[j] += int(str_n[:i]+"0"*(length-i-1))
print(*ans)