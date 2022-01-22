# Problem: https://docs.google.com/document/d/10CvPHttRGQ12zW2jlETtRPdXaA1m_5s1MmBTGIa-7_A/edit?usp=sharing

message = input()
u, l , s = '', '', ''

for c in message:
    if c.isupper(): u += c
    if c.islower(): l += c
    if c == ' ': s += c
      
u = ''.join(sorted(u))
l = ''.join(sorted(l)[::-1])

print(u + s + l)
