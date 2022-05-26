# What are loops?
# A loop is a way to repeat a block of code until a condition is met.

# There are two types of loops:
# 1. for loops
# 2. while loops

# For Loops Examples:

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

fruits = ['apple', 'banana', 'orange', 'pear', 'strawberry', 'kiwi', 'grape', 'mango', 'pineapple', 'blueberry']

for l in numbers:
    print(l, fruits[l - 1])

name = 'Adekola'
for letter in name:
    print(letter)

users = [{'name': 'Adekola', 'age': '23'}, {'name': 'Adeyinka', 'age': '24'}, {'name': 'Adamu', 'age': '25'}]
for x in users:
    print(x.get('name'), x.get('age'))

# Exercise:
# 1. Create a list of numbers and print each number.
# 2. Create a list of numbers and print each number squared.
# 3. Create a list of fruits and print each fruit's name, color and taste.

