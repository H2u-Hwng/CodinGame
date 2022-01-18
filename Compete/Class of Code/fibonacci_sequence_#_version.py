# Problem: https://docs.google.com/document/d/1VXCkC8hiVYF-y4-FfkgPeGxdx5ahdd6QPhOpdUgC5IA/edit?usp=sharing

n = int(input())
ch = input()
n1, n2 = 1, 1
count = 0
while count < n:
    print(ch * n1)
    nth = n1 + n2
    n1 = n2
    n2 = nth
    count += 1
