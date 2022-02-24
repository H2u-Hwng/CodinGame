# Problem: https://docs.google.com/document/d/189Mll2wcZ9APxOrXzpxy3nrXuPrO9weFfzdhhg2ZCCI/edit?usp=sharing

c = input()
l = int(input())
if l % 2 == 0: print("CAN'T")
else: print('*'*(l//2) + c + '*'*(l//2))
