# Problem: https://docs.google.com/document/d/1xiYhILArjLlNwgBe_asuUXdmBveBi7J6ff_tjqgeh3o/edit?usp=sharing

n = [int(i) for i in input('Enter a number: ')]

result = 0

for i in n:
    if i % 3 == 0:
        result += i
        
for i in range(len(n) - 1):
    if (n[i] + n[i+1]) % 3 == 0:
        result += int(f'{n[i]}{n[i+1]}')

print(result)
