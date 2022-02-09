# Problem: https://docs.google.com/document/d/1YHc6R-GoARbkeyZrlb6Zk5a9TvKoaKKy6YxtSOGM5cw/edit?usp=sharing

from math import log
n = int(input())
r = log(n,2)
print(int(r) if '.0' in str(r) else -1)
