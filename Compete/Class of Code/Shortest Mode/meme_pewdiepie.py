# Problem: https://docs.google.com/document/d/1g5qOfLmCZD5O0pJPy7AkhiiVL5OEN1uPfJX2DppcISU/edit?usp=sharing

m=input()
s=sum(ord(c)for c in set(m)if c.isalpha())
l=len(m)
print(f'{s%l}/10'if s%l<=10 else'10/10')
