# Railroad cars are made by a number of different manufacturers in Canada. A train company startup purchases cars from several different vendors and uses the following codes to identify railroad cars:

 

# "AMFT", "BT", "CCF", "CNLX", "MI", "MLW", "NSC", "PCC", "HSC", "OCC", "PRO", "TW", "UTDC"

 

# An individual car will use the 4, 3, or 2 letter rail vendor code and a 3 or 4 digit number prefix or suffix to identify individual rail cars. Vendor codes might be all caps or all lower case.

 

# For example, the following codes are valid:

 

# 001AMFT

# 9873BT

# CNLX7815

# hsc224

 

# The following codes are not valid:

 

# bt123mi

# pro123567

# 123NSC456

 

# Write a program that accepts strings supplied by the user and reports whether the train car code is valid or not. Use at least 2 functions. Include an IPO comment for each function. For a full score your program should be of minimum length and work for any input.

 

# Use the following code for the main part of your program:

 

rail_vendor = ["AMFT", "BT", "CCF", "CNLX", "MI", "MLW", "NSC", "PCC", "HSC", "OCC", "PRO", "TW", "UTDC"]

def valid(code, rail_vendor):
  test1 = False
  if code != code.upper() and code != code.lower():
    return False
  code=code.upper()
  for x in rail_vendor:  
    if x in code:
    code_letters = x
    test1 = True
  if test1 == False:
    return False
  if code.find(code_letters) != 0  and code.split(code_letters, 1)[1] != '':
    return false
  if len(code.replace(code_letters, '')) < 2 or len(code.replace(code_letters, '')) > 4 or not str(code.replace(code_letters, '')).isdigit():
    return False
  return True
  

done = False
while not done:
    tc = input("Train Car Code (Q to quit)> ")
    if tc == "Q":
        done = True
    elif valid(tc, rail_vendor):
        print("Train Car Code is valid.")
    else:
        print("Train Car Code is not valid, try again.")

