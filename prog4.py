# Find the sum of all elements in a 3X3 matrix using python.

l1 =[[1,2,3],
     [4,5,6],
     [7,8,9]
     ]

# Initializing total sum
sum=0

# Loop through each element and add to total
for row in l1:
    for element in row:
        sum+=element

# Print the total sum
print(f"Sum of all elements in a matrix = {sum}")
