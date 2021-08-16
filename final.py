# A padlock company makes a wheel based lock that opens when the correct sequence of letters is selected. They want a computer program that will generate all possible codes for locks that use between 3 and 12 letters, and between 2 and 5 code wheels. The letters should all be upper case and should start with 'A', and go up alphabetically to the 12th letter. 

 

# Write a program that generates and counts all possible codes. Your program should ask the user for the number of letters to use and the number of wheels to use. Assume all input is legal input (do not worry about inputs with errors)

 

# Your program should use at least one function. Include IPO comments. For a full score your program should be a minimum number of lines.

 

# For the simplest case, a program run looks like this:

 

# Code letters[3 - 12]> 3
# Code wheels[2 - 5]> 2

# AA
# AB
# AC
# BA
# BB
# BC
# CA
# CB
# CC

# total codes = 9

import string
import itertools

code_letters = input("Code letters[3 - 12]")
while (3 > float(code_letters) or 12 < float(code_letters)) or not float(code_letters).is_integer():
  code_letters = input("Code letters[3 - 12]")
code_wheels = input("Code wheels[2 - 5]")
while (2 > float(code_wheels) or 5 < float(code_wheels)) or not float(code_wheels).is_integer():
  code_wheels = input("Code wheels[2 - 5]")

def print_codes(letters, wheels):
  alphabets= string.ascii_uppercase[:letters] #ex letters=3. will return 'ABC'
  alphabets_list = list(alphabets) #'ABC -> ['A', 'B', 'C']
  combinations = itertools.product(alphabets_list, repeat = wheels) #(A, A, A)
  combinations_string=[] 
  count = 0
  for x in combinations:
    combinations_string.append("".join(x)) #tuples to string
    count+=1
  print('\n'.join(list(combinations_string))) # line breaks
  print (f"total codes = {count}")

print_codes(int(code_letters), int(code_wheels))