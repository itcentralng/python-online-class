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
# numbs = [1, 3, 5, 6, 7, 9]
# for nb in numbs:
#     print(nb)
    
    
#ans 2.

fin = [1, 4, 6, 8, 10]
for gx in fin:
    print(gx**2)   
    
    
#ans 3.

# fruits = [{'name': 'apple', 'color':'Red', 'taste':'sweet'}, {'name': 'mango', 'color': 'green', 'taste': 'not sweet'}, {'name': 'guava', 'color': 'blue', 'taste': 'very sweet'}]
# for f in fruits:
#     #print(f.get('name'), f.get('color'), f.get('taste'))    
    
#     kol = f.get('name') + "   |" + f.get('color') + "   |" + f.get('taste')

#     print(kol) 

print("\n\n\n\n\n")

# While Loops Examples:

import random
import math
from tkinter.messagebox import NO, YES

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
points = 0
while True:
    number = random.choice(numbers)
  
    answer = input("I have a number, can you guess it?: \n")
    if answer == 'exit':
        break
    elif answer == str(number):
        points += 5
        
        print('You got it! and have earned: ', points,  ' points') 
    else:
        points -= 1
        print('Nope, You have lost 1 point, you now have:' +  str(points)) 
    
    # play_again = input("Play again? (y/n): ")
    # if play_again.lower() != "y":
    #     break


# Exercise:
# 1. Upgrade the above game to show the user thier point, assuming every correct guess gives them 5 points and every incorrect guess subtracts 1 point.
# 2. Create a State and Capital game that shows a user a state and asks them to guess the capital. Each time they get it right, they get 5 points and when they get it wrong, they lose 1 point. The user should be able to stop the game when they type in 'exit'.

print('\n\n\n')

##############################################################################################################################################################################
#############################################################################################################################################################################



state = {'Abia': 'Umuahia',
                'Adamawa': 'Yola',
                 'Akwa Ibom': 'Uyo',
                 'Anambra': 'Awka',
                 'Bauchi': 'Bauchi',
                 'Bayelsa': 'Yenagoa',
                 'Benue': 'Makurdi',
                 'Borno': 'Maiduguri',
                 'Cross River': 'Calabar',
                 'Delta': 'Asaba',
                 'Ebonyi': 'Abakaliki',
                 'Edo': 'Benin City',
                 'Ekiti': 'Ado-ekiti',
                 'Enugu': 'Enugu',
                 'Gombe': 'Gombe',
                 'Imo': 'Owerri',
                 'Jigawa': 'Dutse',
                 'Kaduna': 'Kaduna',
                 'Kano': 'Kano',
                 'Katsina': 'Katsina',
                 'Kebbi': 'Birnin Kebbi',
                 'Kogi': 'Lokija',
                 'Kwara': 'Ilorin',
                 'Lagos': 'Ikeja',
                 'Nasarawa': 'Lafia',
                 'Niger': 'Minna',
                 'Ogun': 'Abeokuta',
                 'Ondo': 'Akure',
                 'Osun': 'Oshogbo',
                 'Oyo': 'Ibadan',
                 'Plateau': 'Jos',
                 'River': 'Port Harcourt',
                 'Sokoto': 'Sokoto',
                 'Taraba': 'Jalingo',
                 'Yobe': 'Damaturu',
                 'Zamfara': 'Gusau',
            }
key_state =  list(state.keys())
points = 0
wrong_answers = 0


while True:
    req = random.choice(key_state)
        
    if wrong_answers == 10:
        me = input('         Do you wish to continue the game? ' + '\n y=YES \n n=NO \n >>>>  ')
       
    
    
        if me == "n":
            print('Weldone, Play again soon \n\n')
            break
        else:
            wrong_answers = 0
            print('Keep riding')
    
    usd = input("What is the Capital of: " +  req + '\n\n')


    if usd == 'q':
        ask = input('                Do you really want to quit the game.   [Y / N] \n\n')
        #########################  NOTICE  ##############################################
        if ask.upper() == 'Y':
            print(' Look forward to you playing soon again. cheers!')     #>>>>statement is not active
            break
        else:
            print('\n Goodluck! \n')
            continue
     
    elif usd.casefold().replace(" ", "") == state.get(req).casefold().replace(" ", ""):
 
       #YOU CAN USE THIS METHOD TOO $$$$$$$$$$$$$$>>>>>>>#ASSIGNING OF A VARIABLE TO THE STATEMENT 
       #    x = usd.replace("", "*")
       
        
        points += 5
        wrong_answers = 0
        
        print(' Correct! and have earned: ' +  str(points) + ' points \n') 
    else:
        points -= 1
        wrong_answers += 1
        print(' Wrong answer, try again! You have lost 1 point' + " " + str(points) + '\n')
        
        
########>>>>>>>Add a function that will exit the game and also restart the game automatically<<<<#####################################################################











######################################################################################################################################
#eg 4 A program that print out speed, from the given details of distance and time.
print('  ****                 NEW GAME             ****  \n\n\n')
while True:
    distance = float(input("Enter the distance to work in kilometers: \n"))

    time = float(input(" Enter time of arrival in hours: \n"))

    speed = distance/time

    print(" Speed is: ", speed, "kph \n\n")

    check = input(
        "Do you want to quit or start again? enter Y to restart or another key to end: ")
    if check.upper() == "Y":  # go back to the top
        continue
    else:
        print("    Bye...")
        break
