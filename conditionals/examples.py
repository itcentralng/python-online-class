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

database = {'username': 'admin', 'password': 'admin'}

username = input("Username: ")
password = input("Password: ")

if username == database['username'] and password == database['password']:
    print("Access granted")
elif password != database['password'] and username != database['username']:
    print("Access denied")
elif username != database['username']:
    print("Username incorrect")
else:
    print("Password incorrect")

# Example 2
"""
Create a program that asks a user for their name and age.
If they are 18 or older, print "You can vote"
If they are younger than 18, print "You can't vote"
"""