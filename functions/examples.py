from random import randint
import time


def countTo5():
    numbers = [1, 2, 3, 4, 5]
    for n in numbers:
        print(n)
        time.sleep(1)

# # countTo5()

# # Game 1

# while True:
#     print('Are you ready?')
#     countTo5()
#     print('Go!')
#     answer = input('Are you ready to play again? (y/n): ')
#     if answer.lower() == 'n':
#         break

# # Game 2

# while True:
#     print('Are you ready?')
#     countTo5()
#     print('Go!')
#     number = randint(1, 10)
#     answer = input('I have a number between 1 and 10, guess it: ')
#     if answer.lower() == 'exit':
#         break
#     elif answer == str(number):
#         print('You got it!')

def getCurrentdate():
    return time.strftime("%d/%m/%Y")

print('Todays date is ', getCurrentdate())

def getAbbrevation(text):
    letters = ''
    for word in text.split():
        letters += word[0]
    return letters.upper()

print(getAbbrevation('Nigerian Air Force College of Nursing Science'))
print(getAbbrevation('Nigerian Air Force Officers Wives Association'))

def getFirstLetter(text='A'):
    return text[0]

print(getFirstLetter())

# Exercise:
# 1. Create a function that takes a list of numbers and returns a new list with only the even numbers.
# 2. Create a function that takes a list of numbers and returns a new list with only the odd numbers.