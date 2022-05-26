# What are loops?
# A loop is a way to repeat a block of code until a condition is met.

# There are two types of loops:
# 1. for loops
# 2. while loops

# For Loops Examples:

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# fruits = ['apple', 'banana', 'orange', 'pear', 'strawberry', 'kiwi', 'grape', 'mango', 'pineapple', 'blueberry']

# for l in numbers:
#     print(l, fruits[l - 1])

# name = 'Adekola'
# for letter in name:
#     print(letter)

users = [{'name': 'Adekola', 'age': '23'}, {'name': 'Adeyinka', 'age': '24'}, {'name': 'Adamu', 'age': '25'}]
for x in users:
    print(x.get('name'), x.get('age'))

# Exercise:
# 1. Create a list of numbers and print each number.
# 2. Create a list of numbers and print each number squared.
# 3. Create a list of fruits and print each fruit's name, color and taste.

#ans 1.
numbs = [1, 3, 5, 6, 7, 9]
for nb in numbs:
    print(nb)
    
    
#ans 2.

fin = [1, 4, 6, 8, 10]
for gx in fin:
    print(gx**2)   
    
    
#ans 3.

fruits = [{'name': 'apple', 'color':'Red', 'taste':'sweet'}, {'name': 'mango', 'color': 'green', 'taste': 'not sweet'}, {'name': 'guava', 'color': 'blue', 'taste': 'very sweet'}]
for f in fruits:
    #print(f.get('name'), f.get('color'), f.get('taste'))    
    
    kol = f.get('name') + "   |" + f.get('color') + "   |" + f.get('taste')

    print(kol) 

print("\n\n\n\n\n")

# While Loops Examples:

import random

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

while True:
    number = random.choice(numbers)
    answer = input("I have a number, can you guess it?: \n")
    if answer == 'exit':
        break
    elif answer == str(number):
        print('You got it!')
    else:
        print('Nope, try again')

# Exercise:
# 1. Upgrade the above game to show the user thier point, assuming every correct guess gives them 5 points and every incorrect guess subtracts 1 point.
# 2. Create a State and Capital game that shows a user a state and asks them to guess the capital. Each time they get it right, they get 5 points and when they get it wrong, they lose 1 point. The user should be able to stop the game when they type in 'exit'.
