# Problem: https://docs.google.com/document/d/1j5SigrUGSks7uG2iQDNT5B0axwjEsGtyInZ4reJk6H4/edit?usp=sharing

import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
b=['-'*(n+2)]
for i in range(n):
    b.append('-'+input()+'-')
b.append('-'*(n+2))
#print(b)
for i in range(1,n+1):
    for j in range(1,n+1):
        #print(i,j,b[i][j])
        if(b[i][j]=='-'):
            print([b[i-1][j-1],b[i-1][j],b[i-1][j+1],b[i][j-1],b[i][j+1],b[i+1][j-1],b[i+1][j],b[i+1][j+1]].count('*'),end='')
        else:
            print(b[i][j],end='')
    print('')
