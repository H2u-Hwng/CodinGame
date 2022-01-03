import math

length = int(input())
rpm = int(input())

print(f'{length * rpm * 2 * math.pi / 60:.2f}')
