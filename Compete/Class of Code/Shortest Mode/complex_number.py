# Problem: https://docs.google.com/document/d/13H-U_pg_06XJBsdH0he5MMQwO8hX5TfECifp1yQ1-J8/edit?usp=sharing

import cmath
s=input()
i=s.find('+')
z=complex(float(s[:i]),float(s[i+1:-1]))
print(f'{z.real:.1f} {z.imag:.1f} {abs(z):.1f}')
