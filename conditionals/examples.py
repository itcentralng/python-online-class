# if condition:
    # do something

# Example

numbers = [1, 2, 3, 4, 5]

if 6 not in numbers:
    print("Hello world 6 times")

if 4 in numbers:
    print("Hello world 4 times")

print('\n\n\n')

if 1 in numbers:
    print("Hello world 1 time")
elif 2 in numbers:
    print("Hello world 2 times")
elif 3 in numbers:
    print("Hello world 3 times")

# database = {'username': 'admin', 'password': 'admin'}

# username = input("Username: ")
# password = input("Password: ")

# if username == database['username'] and password == database['password']:
#     print("Access granted")
# elif password != database['password'] and username != database['username']:
#     print("Access denied")
# elif username != database['username']:
#     print("Username incorrect")
# else:
#     print("Password incorrect")

# Example 2
"""
Create a program that asks a user for their name and age.
If they are 18 or older, print "You can vote"
If they are younger than 18, print "You can't vote"
"""
"""
example 1
name = input("what is your name? ")
age = input(name + " What is your age? ")

age = int(age)

if age >= 18:
    print(name + " You can vote")
else:
    print("You can't vote")    
    
    """
    
    
    #eg2:
        
# db = {'name': 'alex',  'fingerprint': '2'}
        
# mt = input("Input username: ")
# mac = input("Your ID: ")
# pt = input("Code: ")
        
# if mac == db['name'] and pt == db['fingerprint']:
#     print('Youre welcome ' + mt)
# elif mac != db['name'] and pt != db['fingerprint']:
#     print("Access denied,  runaway from here " + mt)
# else:
#     print("youre an imposter! " + mt)    
    
    
   # eg3:
   
# cars = ['lexus', 'toyota', 'jeep', 'volkwagen', 'Audi']
# xn = str(cars).casefold()
# imp = input("What type of car do you want? ")

# if imp in xn:
#     print("CAR AVAILABLE")
# else:
#     print('CAR UNAVAILABLE')
    
    #eg4:
################################################################################
###############################################################################
##############################################################################
#numbers = (1, 2, 3, 4)
'''
even_no = ('2', '4', '6', '8') 
odd_no = ('1', '3', '5', '7')

hx = input("input any number? ")
 
if hx in even_no:    #######>>>>>>>>>>#######
    print("Even number") 
elif hx in odd_no:
    print("Odd number")
else:
    print("Number don't exist") 
 #########################################################################################
 ##########################################################################################   
'''    
    #eg5:
# a = 2
# b = 5
# c = 4

# if a < b and a < c:
# 	print(a, 'is less than', b, 'and', c)

#eg6:

# i = 1
# while i < 100:
#   #print(i)
# #i += 1

for numbs in range(0, 101, 1):
    print(numbs)
    
    print('\n\n\n')
    
print('\n\n\n\n\n')    
    
# num = int(input("   INPUT ANY NUMBER TO KNOW IF ITS EVEN NUMBER OR ODD NUMBER: "))
# if (num not in numbs):
#     print("Number is not within range, try another. ")
# elif (num % 2 ) == 0:
#     print("  THIS IS AN EVEN  NUMBER! NO DOUBT. ")
# else:
#     print("  OoopS, WE GOT AN ODD NUMBER. ")         

#eg7:

print('\n\n\n\n\n')    
    
# num = int(input("   INPUT ANY NUMBER TO KNOW IF ITS EVEN NUMBER OR ODD NUMBER: "))
# if (num not in range(0, 10000)):
#     print(" >>>>Number is not within range, try another. ")
# elif (num % 2 ) == 0:
#     print(" >>>>THIS IS AN EVEN  NUMBER! NO DOUBT. ")
# else:
#     print(" >>>> OoopS, WE GOT AN ODD NUMBER. ")   
    
    
#######################################################################################################
#pw = "123"

while True:
    
    dox = input(" INPUT PASSWORD: ")
    if dox == "123":
        print(" SUCCESSFUL ") 
    break
else:
    print(" WRONG PASSWORD, TRY AGAIN")       
    
 ###################################################################################         


 
     
      
