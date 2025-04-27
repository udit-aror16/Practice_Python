# Python Program to calculate the square root
 
num = float(input("Enter the number for which you want to print the square root : "))

num_sqrt = num**0.5
print(f"The square root of {num} is {num_sqrt}")
            
# Find square root of real or complex numbers

import cmath

# num1 = 1 + 2j

num1 = eval(input("Enter the complex number of which you want the square root : "))
num1_sqrt = cmath.sqrt(num1)
print(f"The square root of {num1} is {num1_sqrt}")
