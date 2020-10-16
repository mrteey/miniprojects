# Question 1
'''
Write an if statement that checks th validity
of a user as they try to login to a website
you have created. Pick the data type of your 
choice to store the users information.
'''

users_db = {'usman@gmail.com':{'id':1, 'password':'pass'},
 'testman@yahoo.com':{'id':2, 'password':'passx'}}

email = 'usman@gmail.com'
password = 'passxx'

if email.lower() in users_db:
    if password == users_db.get(email.lower()).get('password'):
        print('Login successful')
    else:
        print('Invalid Password')
else:
    print('Invalid Email')

#Question 2:
"""
create three variables 
a, b and c 
with the data 'apple', 'ball' and 3 consequetively

check if 'app' is in the variable a,
if it is you check again to see if
the variable b is a string, if it is a string you
print the variable b if it is not, you print the 
variable a. However, if 'app' not in 
the variable a print 'oops'.
"""

a = 'apple'
b = 'ball'
c = 3

# a, b, c = 'apple', 'ball', 3

if 'app' in a:
    if type(c) == int:
        print(b)
    else:
        print(a)
else:
    print('oops')