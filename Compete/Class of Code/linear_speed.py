# Problem: https://docs.google.com/document/d/127lUJmTdCCoRiTx5tS6_EDpxM5EWwUOcD_68shaeZrE/edit?usp=sharing

import math

length = int(input())
rpm = int(input())

print(f'{length * rpm * 2 * math.pi / 60:.2f}')
