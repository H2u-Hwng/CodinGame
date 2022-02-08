# Problem: https://docs.google.com/document/d/1mEX7fdbHTi7NmEZo7IceaxA64NmuDUZaDUBjBRcWXAk/edit?usp=sharing

a,b =[int(i) for i in input().split()]
print(['Not amicable','Amicable'][sum([i for i in range(1,a//2+1)if a%i==0])==b and sum([i for i in range(1,b//2+1)if b%i==0])==a])
