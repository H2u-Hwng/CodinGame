# Problem: https://docs.google.com/document/d/1alGBhMiAn4mX9wCjy7H6Z83arwKeGNG7-iJpjbiyboA/edit?usp=sharing

words_list = input().strip().split()

result = []

for word in words_list:
    counting = len([char for char in word if char.isalpha()])
    
    if counting > 0:
        result += ['A'+'m'*counting]
        
    result += [word]
    
print(*result)
