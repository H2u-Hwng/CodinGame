# Problem: https://docs.google.com/document/d/1Sz1cWKsiQzQUOjC76TzFcOQGYEZIPvQuWg6NjQ0B6VA/edit?usp=sharing

def print_roman(number):
    dict = {1:"I", 4:"IV", 5:"V", 9:"IX", 10:"X", 40:"XL", 50:"L",
            90:"XC", 100:"C", 400:"CD", 500:"D", 900:"CM", 1000:"M"}
      
    for i in sorted(dict, reverse = True):
        result = number // i
        number %= i
  
        while result:
            print(dict[i], end = "")
            result -= 1

print_roman(int(input()))
