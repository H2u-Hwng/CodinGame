# Problem: https://docs.google.com/document/d/1GjpUWai4xZf3ZN27Q9SH5ZeHX3IekxguBT-asRemkKw/edit?usp=sharing

n = int(input())
ingre = input().split()
p = int(input())
order = []
for i in range(p):
    order += input().split()
if len(order) > len(ingre):
    print('NO')
else:
    check = all(i in order for i in ingre)
    if check:print('YES')
    else:print('NO')
