# Problem: https://docs.google.com/document/d/1rUBGLuwEHxbB6cDMsgKNhe-4JvpOdCRxI3Qd_ztbsxc/edit?usp=sharing

word = input('Enter a word: ') # prompt the user for a word

result = 'false' # initialize a result

for index in range(len(word) - 1):
    if word[index].lower() == word[index + 1].lower():
        result = 'true'
        break       
    
print(result) # display the result
