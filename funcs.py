from random import choice

def fullname(fname, lname):
    return fname+' '+lname

xname = 'Abdul'
sname = 'Maska'

name = fullname(xname, sname)

print(name)


def find_prime(numbers):
    '''
    This function returns the first
    prime number from a list of numbers.
    *numbers:
    This parameters expects a list or a 
    tuple of numbers
    '''
    for number in numbers:
        for i in range(2, number):
            print(i)
            is_prime = True
            if number > 2:
                print('> 2')
                if number%i == 0:
                    print('not prime')
                    is_prime = False
            if is_prime:
                print('prime found: ', i)
                return number
    return 'No prime found'

print(find_prime([10, 10, 20, 30]))

# Do something with a prime number

prime = find_prime([12, 3, 4, 6])

print(prime)

print('\n')
print('\n')
print('\n')

def order_this(data):
    '''
    This function returns an ordered data.
    :data: expects a list of strings
    '''
    alphabets = {}
    data.sort()
    for d in data:
        if d[0] not in alphabets:
            alphabets[d[0]] = []
        alphabets[d[0]].append(d)
    return alphabets

data2 = ['Banana', 'Apple', 'Cup', 'Ball', 'Air', 'Class', 'Diamond', 'Silver', 'Baloon', 'Chicken', 'PS2']
data3 = ['Cup Cakes', 'Apple Pie', 'Glass', 'Ball', 'Air', 'Class', 'Diamond', 'Silver', 'Baloon', 'Chicken', 'PS2']

print(order_this(data3))

def add_numbers(first, second):
    return first+second

print(add_numbers(10, 2))

number = add_numbers(10, 2)
print(number)

def makesmaller(some_big_string):
    return some_big_string.lower()

s = 'AHMAD'

print(makesmaller(s))

print(makesmaller('AHMAD'))


def cleanWord(word):
    '''
    Takes string as arguement and removes any preposition
    returning a simplified version of that string with no prepositions.
    e.g. Knowledge and Understand of the World returns Knowledge Understanding World
    '''
    if word.lower() not in ['and', 'of', 'to', 'the', '&', 'in', 'on', 'by']:
        return True
    return False

def alphabet(word):
    '''
    Takes a string as an arguement and return
    an abbreviated version of that string. e.g.
    Knowledge Understanding Word returns KUW
    '''
    if len(word) > 0:
        return word[0].upper()

def wordstrip(word):
    '''
    Takes a string as arguement,
    remove all prepositions and abbreviate the returned clean string version.
    e.g. e.g. Knowledge and Understand of the World returns KUW
    '''
    if len(word.split(' ')) > 2:
        if len(word) > 20:
            new_word = ""
            for i in word.split(' '):
                if cleanWord(i):
                    new_word += alphabet(i)
            return new_word
    return word

x = wordstrip('cultural and creative art')
print(x)


print('\n')
print('\n')
print('\n')



shop = []
# [{'id':'1', 'name':'carrot', 'price':100, 'stock':2}]

def add_product(name, price, stock):
    product = {'id':str(len(shop)+1), 'name':name, 'price':price, 'stock':stock}
    shop.append(product)

add_product('carrot', 10, 2)
add_product('banana', 100, 5)
add_product('orange', 200, 10)
add_product('cashew', 150, 5)
add_product('pineapple', 200, 15)

print(shop)

# product = {'id':'1', 'name':'carrot', 'price':100, 'stock':2}

print('\n')
print('\n')
print('\n')
print('\n')


cart = {}
# {'1':{'unit':2, 'price':100, 'name':'carrot'}, '2':{}}

def add_to_cart(product):
    '''
    function takes a dict of product
    and add it to the shopping cart.
    :product: looks like 
    {'id':'1', 'name':'carrot', 'price':100, 'stock':2}
    '''
    if product.get('id') in cart:
        cart_product = cart.get(product.get('id'))
        # {'unit':2, 'price':100, 'name':'carrot'}
        if cart_product.get('unit') < product.get('stock'):
            cart_product['unit'] += 1
    else:
        cart_product = {'unit':1, 'price':product.get('price'), 'name':product.get('name')}
        cart[product.get('id')] = cart_product


for i in range(5):
    add_to_cart(choice(shop))
# add_to_cart(product)

print(cart)



print('\n')
print('\n')
print('\n')
print('\n')
def checkout(cart, is_paid=False):
    #cart = {'1':{'unit':2, 'price':100, 'name':'carrot'}}
    '''
    total: 145000
    products: [{'unit':2, 'total':200, 'name':'carrot'}]
    if is_paid:Thank your for your patronage!
    '''
    total = 0
    products = [{'unit':cart.get(product).get('unit'), 'total':cart.get(product).get('unit')*cart.get(product).get('price'), 'name':cart.get(product).get('name')} for product in cart]
    for product in products:
        total+= product.get('total')
    thanks = 'Thank you for your patronage!' if is_paid else 'Please ensure to pay!'
    return f'total: {total}\nproducts: {products}\n{thanks}'

print(checkout(cart, True))

print('\n')
print('\n')
print('\n')
print('\n')

# {
# '1':{'unit':2, 'price':100, 'name':'cashew'},
#  '2':{'unit':2, 'price':100, 'name':'carrot'}
# }
# remove('1', 2)
# {
#  '2':{'unit':2, 'price':100, 'name':'carrot'}
# }
# 2 units of cashew removed succefully
# product with id '1' not in cart
# remove('2', 1)
# {
#  '2':{'unit':1, 'price':100, 'name':'carrot'}
# }
# 1 unit of carrot removed succefully
# product with id '2' not in cart


def sayHi(fname, lname):
    print(f'Hi {fname} {lname}')

sayHi('Ahmad', 'Maska')

def productName(product_id):
    for product in shop:
        if product.get('id') == product_id:
            return product.get('name')
    return f'Product with id {product_id} does not exist'

print(productName('12'))

print('\n')
print('\n')
print('\n')

def removeProduct(product_id, unit=1):
    for num in cart:
        if product_id == num:
            cart[product_id]['unit'] -= unit
            return f"{unit} unit(s) of {cart[product_id]['name']} removed successfully!"
print(cart)
print('\n')
print(removeProduct('1', 2))
print('\n')
print(cart)

print('\n')
print('\n')
print('\n')
print('\n')

def intro(name, address, age):
    return f"My name is {name}, I live at {address} and I am {age} years old"

def intro2(name, address, age):
    print(f"My name is {name}, I live at {address} and I am {age} years old")

def returnNum(num):
    if num.isdigit():
        return int(num)
    return 0
returnNum('1')

def write(content, name='note.txt'):
    with open(name, 'w') as mynote:
        mynote.write(content)
        mynote.close()
    return 'Done!'
content = 'This is a test'
code = "print('hello world')"
write(content)
write(code, 'test.py')

import csv

from io import StringIO

students = {'1':{'name':'Alex', 'age':'10', 'class':'Primary 2', 'dob':'2020'}, '2':{'name':'John', 'age':'13', 'class':'SS 2', 'dob':'2020'}, '3':{'name':'Abdurrahman', 'age':'16', 'class':'JS 2', 'dob':'2020'}}

content = StringIO()
writer = csv.writer(content)
header = ['name', 'age', 'class', 'dob']
writer.writerow(header)
for student in students:
    writer.writerow([students.get(student).get('name'), students.get(student).get('age'), students.get(student).get('class'), students.get(student).get('dob')])
write(content.getvalue(), 'test.csv')


#QUESTION: 
"""
(a) Mr. Samuel wants a function that will help him add products
to his shop. Each product has a name, price and stock unit.

(b) Mr. Samuel is happy with your function and wants to hire
you to build another function that will help his customers
add products from his shop to their cart.

(c) Now Mr. Samuel is excited and want you to build another 
function that will help his customers calculate how much they
should pay for all the items in their cart.
"""

market = []

def add_products(name, price, stock):
    product = {'id':len(market)+1, 'name':name, 'price':price, 'stock':stock}
    market.append(product)
    return market
add_products('Banana', 10, 2)
add_products('Apple', 20, 3)
add_products('Cashew', 40, 5)
print(market)

print('\n')
print('\n')

cart = {}

# def add_to_cart(product):
#     if product.get('id') in cart:
#         cart_product = cart.get(product.get('id'))
#         if cart_product.get('unit') < product.get('stock'):
#             cart_product['unit'] += 1
#             return cart

# add_to_cart(shop[0])
# print(cart)

def add_to_cart(name, unit):
    #We loop through all item in the market
    #The market looks like this: [{'id':1, 'name':'Banana', 'price':10, 'stock':10}]
    for item in market:
        #item looks like {'id':1,'name':'Banana', 'price':10, 'stock':10}
        if item.get('name') == name:
            #item.get('name') looks like this: 'Banana'
            product = {'name':name, 'unit':unit, 'price':item.get('price')}
            if unit <= item.get('stock'):
                #item.get('stock') looks like this: 10
                if item.get('id') in cart:
                    # item.get('id') looks like: '1'
                    # cart looks like {'1':{'name':'Banana', 'unit':1}}
                    cart[item.get('id')]['unit'] += unit
                    # here we are saying somethign like: cart['1']={'name':'Banana', 'unit':1}
                    item['stock'] -= unit
                    # since item looks like {'id':1,'name':'Banana', 'price':10, 'stock':10}
                    # we are deducting the unit in our argument from the stock above
                    print(f'{unit} unit of {name} added successfully')
                else:
                    cart[item.get('id')] = product
                    item['stock'] -= unit
                    print(f'{unit} unit of {name} added successfully')
            else:
                print(f'There are no up to {unit} units of {name} in this market')

add_to_cart('Cashew', 2)
add_to_cart('Cashew', 2)
add_to_cart('Cashew', 3)
add_to_cart('Banana', 2)
add_to_cart('Apple', 2)
add_to_cart('Banana', 5)

print(cart)
print(market)
add_to_cart('Cashew', 1)
print(cart)
print(market)

print('\n')
print('\n')
print('\n')

def add(num1, num2, num3):
    return num1+num2+num3

def name(fname):
    return fname

print(add(5,4,6))
print(name('Ahmad'))

print('\n')
print('\n')
print('\n')


"""
(a) Mr. Samuel wants a function that will help him add products
to his shop. Each product has a name, price and stock unit.
"""

shop = {}

def shopproduct(product, price=0, stock=0, new_name=None):
    if product in shop:
        # we update the price, theres no point adding to the price
        if price:
            shop[product]['price'] = price
        # We add to the stock, because ideally thats what the user would do
        shop[product]['stock'] += stock
        # because negative stock value is allowed
        # check if current stock value is < 1 and return 0 if true
        # so we dont have any negative stock in the shop
        if shop[product]['stock'] < 1:
            shop.__delitem__(product)
        if new_name:
            shop[new_name] = shop[product]
            shop.__delitem__(product)

        print(f'{product} has been updated')
    else:
        shop[product]={'price':price, 'stock':stock}
        print(f'{product} has been added')

shopproduct('Banana')
print(shop)
shopproduct('Banana', 15, 5, 'Apple')
print(shop)
shopproduct('Milk', 15, 5)
print(shop)
shopproduct('Apple', 15, 5, 'Orange')
print(shop)
shopproduct('Orange', 20, 5)
print(shop)
shopproduct('Orange', 35, -5)
print(shop)
shopproduct('Orange', 35, -5)
print(shop)
shopproduct('Orange', 35, -5)
print(shop)
shopproduct('Orange', 35, 15)
print(shop)
shopproduct('Orange', new_name='Cake')
print(shop)
# shopproduct('Cake', stock=-15)
# print(shop)

print('\n')
print('\n')
print('\n')
print('\n')

print(cart)

def checkout():
    total = 0
    for product in cart:
        total+=cart[product]['price']*cart[product]['unit']
    return total

print('Please pay: ', checkout())

print('\n')
print('\n')
print('\n')

#Exercise
"""
1) Create a function that converts days to hours
2) Create a function that converts hours to minutes 
3) Create a function that converts minutes to seconds
4) Using your functions above convert 20days to seconds
"""