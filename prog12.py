# Python Program to Find Numbers Divisible by Another Number

num_list = [23,56,75,65,80,46,35]
result = list(filter(lambda x:(x%5 == 0),num_list))
# result.sort()
sorted_result = sorted(result)
# result.sort(reverse=True)          # to sort the list in descending order
print(f"Numbers divisible by 5 are {sorted_result}")