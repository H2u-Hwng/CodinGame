# Problem: https://docs.google.com/document/d/1v4CyZQRbrVqFP_kiaTpplPRDxpmldllB7BLxNsWvYiM/edit?usp=sharing

import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

f = int(input())
n = int(input())
not_troll = []
for i in range(n):
    monster = input()
    if monster!="TROLL":not_troll.append(monster)

if 2*len(not_troll)<=f:print("Lot of food")
elif len(not_troll)<=f:print("Just enough food")
else:print("Not enough food")
