'''
*********
PROGRAM 2
*********
Define a function exponents that takes an integer as an argument. The function returns a dictionary where the keys are the integers 2, 3, 4, ..., 11, and the values are the key values raised to the power of the argument passed input.

Reminder: In Python, ** stands for the exponent operator

EXAMPLE OF WHAT SHOULD HAPPEN WHEN THIS RUNS:

exponents(3)
--> returns {2: 8, 3: 27, 4: 64, 5: 125, 6: 216, 7: 343, 8: 512, 9: 729, 10: 1000, 11: 1331}
'''

def exponents(exponent): #do not change this line
  integers = [2,3,4,5,6,7,8,9,10,11]
  exponents = [integer ** exponent for integer in integers]
  #for exponent in integers:
    #return integers ** exponent
  print (exponents.items())



"""
elif program == '2':
  exponent = int(input("Number/power: "))
  print(exponents(exponent))
"""