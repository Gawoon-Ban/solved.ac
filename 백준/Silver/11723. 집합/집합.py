import sys
input = sys.stdin.readline

S = 0
command_num = int(input())
for i in range(command_num):
    command = input().split()
    if command[0] == "add":
        S |= (1 << int(command[1])-1)
    elif command[0] == "remove":
        S &= ~(1 << int(command[1])-1)
    elif command[0] == "check":
        if S & (1 << int(command[1]) -1):
            print("1")
        else:
            print("0")
    elif command[0] == "toggle":

        S ^= (1 << int(command[1])-1)
    elif command[0] == "all":
        S = (1 << 21) -1
    else:
        S = 0