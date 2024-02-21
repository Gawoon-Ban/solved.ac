str = input()
score = 0
index = 0
big = 0
mid = 0
sma = 0
while True:
    if index >= len(str)-1:
        break
    for i in range(index,len(str)):
        if str[i] == "[":
            big += 1
        elif str[i] == "{":
            mid += 1
        elif str[i] == "(":
            sma += 1
        elif str[i] == "]":
            big -= 1
        elif str[i] == "}":
            mid -= 1
        elif str[i] ==")":
            sma -= 1
        else:
            index +=1
            break
        index += 1
    if big*3 + mid*2 + sma > score:
        score = big*3 + mid*2 + sma 
print(score)