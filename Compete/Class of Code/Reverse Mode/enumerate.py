# Problem: https://docs.google.com/document/d/1j4_KhstoXHHZXG-8MIM7wFvxHpUDeyzID98Urs3d7O0/edit?usp=sharing

s = input().replace(' ','')
n = int(input())

answer = ""

for i, char in enumerate(s):
    if i%(n+1):
        answer += char.lower()
    else:
        answer += char.upper()

print(answer)
