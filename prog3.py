# Write a python program to check if a number is prime or not : 

# function to check if a number is prime 
def is_prime(num):
    if num <= 1:
        return False # 0 and 1 are not prime
    for i in range(2,int(num**0.5) + 1): # Check up to the sqaure root of the number
        if num % i == 0:
            return False
    return True 
    
# Take input from the user 
number = int(input("Enter a number: "))

# Check and display result
if is_prime(number):
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")