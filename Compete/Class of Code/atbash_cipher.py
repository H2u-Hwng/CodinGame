# Problem: https://docs.google.com/document/d/11nj2NAdvRQVzaOBxild7HgcNX3kkW7IQ7RjB1R-nsrM/edit?usp=sharing

word = input()

for char in word:
    print(chr(ord('z') + ord('a') - ord(char)), end = '')
