# Problem: https://docs.google.com/document/d/1xFnnZimyYLKyrkscNbJiPV11gSITEZ_uDVSTiJ6Nll0/edit?usp=sharing

bad_text = input('Enter a bad text: ')

formated_text = bad_text.replace("4","a").replace("0","o").replace("3","e").replace("1","i")

result = ''.join(char for char in formated_text if char.isalpha() or char == ' ')
print(result if len(result) > 0 else "IRRECOVERABLE")
