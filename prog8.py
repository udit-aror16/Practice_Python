# Write a function to find the area of a right angled triangle rounded off to two decimal places.

def triangle_area(base,height):
    area=(1/2*base*height)
    return area

b=float(input("Enter the value for the base: "))
h=float(input("Enter the value for the height: "))
print(triangle_area(b,h))


