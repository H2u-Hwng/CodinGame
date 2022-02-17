# Problem: https://docs.google.com/document/d/1HWHsFle6KD2sWFyECsEwLD9M4ciJgltD3NeF9oKOckI/edit?usp=sharing

u = ''.join([c for c in input() if c in '+0123456789'])
if u.startswith('+8790'):
    u = u[4:]
elif u.startswith('+879'):
    u = '0' + u[4:]
print(u[:3],u[3:6],u[6:9],u[9:])
