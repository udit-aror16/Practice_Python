# Program to check if a number is prime or not

# num = 29
num = int(input("Enter the number: "))

flag = False 

if (num == 0) or (num == 1):
    print(num,"is not a prime no.")
elif num > 1:
    for i in range(2,num):
        if (num % i == 0):
            flag = True
            break

    if flag:
        print(f"{num} is not a prime number.")
    else:
        print(f"{num} is a prime number.")
