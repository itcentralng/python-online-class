unique_numbers = {1, 2, 2, 3, 3}
print(unique_numbers)
unique_numbers.add(4)
print(unique_numbers)
unique_numbers.clear()
print(unique_numbers)
unique_numbers1 = {1, 2, 3}
unique_numbers2 = {1, 2, 3, 4}
unique_numbers3 = {1, 2, 3, 4, 5, 6}

print(unique_numbers3.difference(unique_numbers1, unique_numbers2))

unique_numbers3.difference_update(unique_numbers1)
print(unique_numbers3)