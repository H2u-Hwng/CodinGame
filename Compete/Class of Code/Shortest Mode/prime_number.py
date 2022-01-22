# Problem: https://docs.google.com/document/d/1gF7im-ezILjAFdRV18mNsov4w_dKhzt9jAL_Dy-Nrlc/edit?usp=sharing

n = int(input())

def is_prime(x):
    return x > 1 and all(x % i for i in range(2, x))

primes = []
for i in input().split():
    if is_prime(int(i)):
        primes += [int(i)]

from collections import Counter
for k,v in Counter(primes).items():
    if v==2:
        print(k)
