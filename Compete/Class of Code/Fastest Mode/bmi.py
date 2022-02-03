# Problem: https://docs.google.com/document/d/14hdEPbNB9BAFSLCCt3WUXs8RcFFyU4V3G68vnUDv-sE/edit?usp=sharing

from math import ceil

mass, height = [int(i) for i in input().split()]
height = height/100
bmi = mass / height**2
if bmi < 18.5:
    print('UNDERWEIGHT', ceil(18.5*height**2 - mass))
elif 18.5 <= bmi < 25:
    print('HEALTHY', 0)
else:
    if 25 <= bmi < 30:
        print('OVERWEIGHT', end=' ')
    else:
        print('OBESE', end = ' ')
    print(ceil(mass - 25*height**2))
