# Problem: https://docs.google.com/document/d/1_zXIH-S9gpbwBQonxluzGqheElFe1lpGSl6BJZC5jgU/edit?usp=sharing

n = int(input())
counting = n
for i in range(n):
    snake = input()
    if '-<' not in snake and '>-' not in snake:
        counting -= 1

print(int(counting / n * 100), '%', sep='')
