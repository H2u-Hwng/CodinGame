# Problem: https://docs.google.com/document/d/1fsV8nq15naAZVVC-kZto2swLUxthdcrldLlgoe7TPJc/edit?usp=sharing

columns = int(input('Enter the number of columns: '))
rows = 1

for i in range(columns):
    print(*range(rows, rows + i + 1))
    rows += i + 1
