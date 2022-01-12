# Problem: https://docs.google.com/document/d/1r-IduQY1DUoFZu0imn63zgMQpgrDNDcACl45kaGK7dA/edit?usp=sharing

import math

s = input('Enter a string: ').lower()

l = len(s)

n = int(input('Enter the number of given characters: '))

for _ in range(n):
    c = input('Enter a character: ')

    print(f'{math.ceil(s.count(c) / l * 100)}%')
