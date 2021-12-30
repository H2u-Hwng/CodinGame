# Problem: https://docs.google.com/document/d/1uB207i3iXy02Mo6LahbYhOq26SsXe21nHHDse-xLyr0/edit?usp=sharing

n = int(input())
p = int(input())
c = int(input())
r = int(input())

t = 0

for i in range(1, n + 1):
    t += p + c + ((i - 1) * 2) + r

print(t)
