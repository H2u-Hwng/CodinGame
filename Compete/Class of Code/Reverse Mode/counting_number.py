# Problem: https://docs.google.com/document/d/1aepdA4LCCAjNw6me8qBlsQoqVgIuxb8bSSFMMJyZh5Y/edit?usp=sharing

i = input()
s = set(i)
for c in sorted(s):
    print(i.count(c), c, sep='', end='')
