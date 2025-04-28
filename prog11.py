# Program to check Armstrong numbers in a certain interval

lower = 100
upper = 5000

for num in range(lower,upper + 1):
    temp = str(num)
    order = len(temp)
    sum = 0
    for i in temp:
        sum += (int(i)**order)
    if num == sum:
        print(num)

