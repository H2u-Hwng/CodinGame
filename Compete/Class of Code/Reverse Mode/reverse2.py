# Problem: https://docs.google.com/document/d/1xWSd5-fB5jyp0YKk317iCoAde4E-o_prHvEKP2UuN0s/edit?usp=sharing

x = int(input())

for i in range(1, x + 1):
    print([f"{'*' * x}", f"{' ' * (x - i)}{'*' * i}"][x%2])
