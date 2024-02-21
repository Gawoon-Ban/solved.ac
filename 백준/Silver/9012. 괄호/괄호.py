def is_VPS(list_):
    stack = []
    for char in list_:
        if char == '(':
            stack.append(char)
        elif char == ')' and stack and stack[-1] == '(':
            stack.pop()
        else:
            print("NO")
            return
    if not stack:
        print("YES")
    else:
        print("NO")
    
num = int(input())
strings = []

for i in range(num):
    string = input()
    strings.append(string)

for j in strings:
    is_VPS(j)
