import sys

input = sys.stdin.readline

pros = []

pro = input().split()
right_pros = []

while pro[0] != '-1':
    pros.append(pro)
    if pro[2] == 'right':
        right_pros.append(pro)
    pro = input().split()


penalty =0
for i in right_pros:
    pro_name = i[1]
    right_time = i[0]
    wrong_num = 0
    for j in pros:
        if j[1] == pro_name and j[2] == 'wrong':
            wrong_num += 1
    penalty += int(right_time) + wrong_num * 20

print(len(right_pros), penalty)