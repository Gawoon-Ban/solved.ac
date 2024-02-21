import sys

command = sys.stdin.readline().strip("\n").split()
while int(command[0]) != 0:
    candy = []
    num = int(command[0])
    total_money = int((float(command[1])+0.0001)*100)
    dp = [0 for _ in range(total_money+1)]
    for i in range(num):
        can = list(sys.stdin.readline().strip("\n").split())
        #칼로리
        can[0] = int(can[0])
        #돈
        can[1] = int((float(can[1])+0.0001)*100)
        candy.append(can)
    for i in range(1,total_money+1):
        cals = []
        for j in range(num):
            if i-candy[j][1]>=0:
                cals.append(dp[i-candy[j][1]]+candy[j][0])
        if len(cals) != 0:
            dp[i] = max(cals)
    print(dp[total_money])    
    command = sys.stdin.readline().strip("\n").split()