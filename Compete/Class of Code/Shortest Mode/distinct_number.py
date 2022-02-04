# Problem: https://docs.google.com/document/d/1V54MeA4FD6F6KPsp2Mnlksssv-6hGQsHVPVFwsd8tng/edit?usp=sharing

l=[[n for n in input()] for _ in range(3)]
for c in l:
    if l.count(c)==1:print(''.join(c))
