#*** Write a Python program to swap two numbers without using third variable :

#Input from the user
a=int(input("Enter the number a: ")) 
b=int(input("Enter the number b: ")) 

#Swappping without third variable
a=a+b
b=a-b
a=a-b

print("After Swapping: ")
print(f"a = {a}")
print(f"b = {b}")



