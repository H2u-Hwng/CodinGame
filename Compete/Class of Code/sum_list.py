# Problem: https://docs.google.com/document/d/1OPPsEo6P4eWuZvNjwnAyatLcYhlYu7DBXVmG_pn3qd0/edit?usp=sharing

length = int(input())

list = []

for i in range(length):
    number = int(input())
    if number % 2 ==0:
        list.append(number * 3)
    else:
        list.append(number * 5)
        
print(sum(list))
