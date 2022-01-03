# Problem: https://docs.google.com/document/d/1KswPBwcu3UIfsW9KPXyHR9pIKHf5TKOb5pctESJbR5k/edit?usp=sharing

s = input('Enter a string: ')

letters_list = [*set(s.lower())]

counting = 1

for letter in letters_list:
    counting *= s.count(letter)

print(counting)
