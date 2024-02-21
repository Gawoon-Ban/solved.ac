import sys
input_ = int(sys.stdin.readline().strip("\n"))
sum = input_
index =2
pre_op = ""
while pre_op != "=":
    input_ = sys.stdin.readline().strip("\n")
    if index%2 ==0:
        if input_ =="+":
            pre_op ="+"
        elif input_=="-":
            pre_op = "-"
        elif input_ =="*":
            pre_op = "*"
        elif input_ == "/":
            pre_op ="/"
        else:
            pre_op ="="
    else:
        if pre_op =="+":
            sum += int(input_)
        elif pre_op=="-":
            sum -= int(input_)
        elif pre_op =="*":
            sum *= int(input_)
        elif pre_op == "/":
            sum //= int(input_)
    index += 1
print(sum)