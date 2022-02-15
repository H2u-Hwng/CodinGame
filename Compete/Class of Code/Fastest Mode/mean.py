# Problem: https://docs.google.com/document/d/1XEoMOrOTK7qwOuyBS5uZOoEEvAFHnI4CsupV67DEpWo/edit?usp=sharing

n = int(input())
l = [int(x) for x in input().split()]
r = sum(l)/len(l)
if '.0' in str(r):
    print(int(r))
else:
    print(r)
