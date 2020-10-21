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


cart = {}
#{'1':{'unit':2, 'price':100, 'name':'carrot'}, '2':{}}

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

shop = []

def add_product(name, price, stock):
    product = {'id':str(len(shop)+1), 'name':name, 'price':price, 'stock':stock}
    shop.append(product)

add_product('carrot', 10, 2)
add_product('banana', 100, 5)
add_product('orange', 200, 10)
add_product('cashew', 150, 5)

print(shop)

# product = {'id':'1', 'name':'carrot', 'price':100, 'stock':2}

print('\n')
print('\n')
print('\n')
print('\n')

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
    if is_paid:Thank your for your business
    '''
    total = 0
    products = [{'unit':cart.get(product).get('unit'), 'total':cart.get(product).get('unit')*cart.get(product).get('price'), 'name':cart.get(product).get('name')} for product in cart]
    for product in products:
        total+= product.get('total')
    thanks = 'Thank you for your patronage!' if is_paid else 'Please ensure to pay!'
    return f'total: {total}\nproducts: {products}\n{thanks}'

print(checkout(cart, True))
    