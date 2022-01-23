# Problem: https://docs.google.com/document/d/1P7iKN0rPEEiGRuxATeAV0ZuuEjUzyq421DkHmzFtMGI/edit?usp=sharing

x=int(input())
for i in range(int(input())):
    f,t,c=input().split()
    if x>=int(f) and x<=int(t):print(c);break
