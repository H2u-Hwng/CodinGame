# Problem: https://docs.google.com/document/d/13bhhvGkor9TIkcTpanK9umbDmMd478HOWh5I40mp-oE/edit?usp=sharing

a,b=map(int,input().split())
c,d=map(int,input().split())
for i in range(a,b+1):
    if i in range(c,d+1):print('Overlap');break
else:print('Not overlap')
