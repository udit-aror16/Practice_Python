# Write a function to add 10 to a given number.

num=int(input("Enter the number : "))

def add_ten(n):
    n+=10
    return n

print(add_ten(num))