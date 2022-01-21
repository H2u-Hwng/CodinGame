# Problem: https://docs.google.com/document/d/16Wd9v3eGH7VW6n-utr-zM7vKLv8R0bYrAXi65aMaQHo/edit?usp=sharing

t = input()

a = ''
b = ''
for c in t:
    if c.isupper():
        a += c
    else:
        b += c
        
print(a)
print(b)
