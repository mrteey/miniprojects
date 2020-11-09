import random

class Shoppingcart:
    def __init__(self, cart, market):
        # cart will be an empty {} when constructed
        # {}
        # market will be an empty [] when constructed
        # []
        self.cart = cart
        self.market = market
    def add_to_cart(self, name, unit):
        #We loop through all item in the market
        #The market looks like this: [{'id':1, 'name':'Banana', 'price':10, 'stock':10}]
        for item in self.market:
            #item looks like {'id':1,'name':'Banana', 'price':10, 'stock':10}
            if item.get('name') == name:
                #item.get('name') looks like this: 'Banana'
                product = {'name':name, 'unit':unit, 'price':item.get('price')}
                if unit <= item.get('stock'):
                    #item.get('stock') looks like this: 10
                    if item.get('id') in self.cart:
                        # item.get('id') looks like: '1'
                        # cart looks like {'1':{'name':'Banana', 'unit':1}}
                        self.cart[item.get('id')]['unit'] += unit
                        # here we are saying somethign like: cart['1']={'name':'Banana', 'unit':1}
                        item['stock'] -= unit
                        # since item looks like {'id':1,'name':'Banana', 'price':10, 'stock':10}
                        # we are deducting the unit in our argument from the stock above
                        print(f'{unit} unit of {name} added successfully')
                    else:
                        self.cart[item.get('id')] = product
                        item['stock'] -= unit
                        print(f'{unit} unit of {name} added successfully')
                else:
                    print(f'There are no up to {unit} units of {name} in this market')
    def checkout(self):
        total = 0
        for product in self.cart:
            total+=self.cart[product]['price']*self.cart[product]['unit']
        print('Amount : ', total)
        return total
    

ahmadscart = Shoppingcart({}, [{'id':1, 'name':'Apple', 'price':10, 'stock':10}])
ahmadscart.add_to_cart('Apple', 2)
ahmadscart.checkout()
alaminscart = Shoppingcart({}, [{'id':1, 'name':'Apple', 'price':10, 'stock':10}])
alaminscart.add_to_cart('Apple', 1)
alaminscart.checkout()


print('\n')
print('\n')
print('\n')

class Person:
    """
    CLASS PERSON:
        constructor: name, age, address
        methods: introduction(), friends(), add_a_friend(), remove_a_friend()
    """
    def __init__(self, name, age, address, _friends=[]):
        self.name = name
        self.age = age
        self.address = address
        self._friends = _friends
    def introduction(self):
        print(f'Hello my name is {self.name}, I am {self.age} years old')
        return self.name
    def friends(self):
        if self._friends:
            print('Here are some of my friends: \n')
            print(', '.join(self._friends))
        else:
            print('I dont have any friends')
        return self._friends
    def add_a_friend(self, name):
        self._friends.append(name)
        print(name, ' added successfully!')
        return name
    def remove_a_friend(self, name):
        self._friends.remove(name)
        print(name, ' removed successfully!')
        return name

person1 = Person('Ahmad Maska', 30, '44A Isa Kaita')
person1.introduction()
person1.friends()
person1.add_a_friend('Alex')
person1.add_a_friend('Abdul')
person1.add_a_friend('Haidar')
person1.friends()
person1.remove_a_friend('Abdul')
person1.remove_a_friend('Haidar')
person1.remove_a_friend('Alex')
person1.friends()

print('\n')
print('\n')
print('\n')
print('\n')
print('\n')

class Questionbank:
    def __init__(self, bank={}):
        self.bank = bank
    def add_question(self, subject, _class, topic, question):
        if subject not in self.bank:
            self.bank[subject] = []
        self.bank[subject].append({'topic':topic, 'class':_class, 'question':question})
        print('Question added successfully!')
        return question
    def generate_questions(self, count, subject=None, _class=None, topic=None):
        quiz = []
        for i in range(count):
            if subject:
                for question in self.bank.get(subject):
                    if _class:
                        if question.get('class').lower() == _class.lower():
                            if topic:
                                if question.get('topic').lower() == topic.lower():
                                    quiz.append(question)
                                    break
                            else:
                                quiz.append(question)
                                break
                    elif topic:
                        if question.get('topic').lower() == topic.lower():
                            quiz.append(question)
                            break
                    else:
                        quiz.append(question)
                        break
            elif _class:
                _subject = random.choice(list(self.bank))
                for question in self.bank.get(_subject):
                    if question.get('class').lower() == _class.lower():
                        if topic:
                            if question.get('topic').lower() == topic.lower():
                                quiz.append(question)
                                break
                        else:
                            quiz.append(question)
                            break
            elif topic:
                _subject = random.choice(list(self.bank))
                for question in self.bank.get(_subject):
                    if topic:
                        if question.get('topic').lower() == topic.lower():
                            quiz.append(question)
                            break
            else:
                _subject = random.choice(list(self.bank))
                question = random.choice(self.bank.get(_subject))
                quiz.append(question)
        print(quiz)
        return quiz

lss_bank = Questionbank()
lss_bank.add_question('Basic Science', 'JS One', 'Digestion', 'Which of the following organ is responsible for digestion?')
lss_bank.add_question('Basic Science', 'JS One', 'Respiration', 'Which of the following organ is responsible for respiration?')
lss_bank.add_question('Basic Tech', 'JS One', 'Lines', 'How many types of lines do we have?')
lss_bank.add_question('Basic Tech', 'JS One', 'Shapes', 'How many types of shapes do we have?')
lss_bank.generate_questions(1, topic='shapes')

print('\n')
print('\n')
print('\n')
print('\n')
print('\n')

class Computer:
    def __init__(self,brand, model,_specs=[]):
        self.brand = brand
        self.model = model
        self._specs = _specs
    def about(self):
        print(f'this is a {self.brand} computer of model {self.model}.')
        return f'this is a {self.brand} computer of model {self.model}.'
    def specs(self):
        print('it has :  \n')
        print(', '.join(self._specs))
    def add_spec(self, spec):
        self._specs.append(spec)
        print(f'{spec} added successfully!!')
laptop = Computer('hp','elite book 250')
laptop.about()     
laptop.add_spec('16 gb RAM')
laptop.add_spec('1TB ssd')
laptop.specs()

print('\n')
print('\n')
print('\n')
print('\n')
print('\n')

# Assignment:
#QUESTION: 
"""
(a) Create a class Shop and a class Cart

(b) Users should be able to add products, remove products and 
update products in their shops.
Each product has an id, name, price and stock.

(c) Users of your Cart class should be able to 
add products from any shop to their cart. This should
automatically modify the products in that particular
shop.

(d) Users should also be able to calculate how much they
should pay for all the items in their cart.

(f) test all with atleast three instances of each class
"""
    

#(a)

class Shop:
    def __init__(self, name):
        self.name = name
        self.content = {}
    def add_product(self, name, price, stock):
        product = {'name':name, 'price':price, 'stock':stock}
        self.content[len(self.content)+1] = product
        # {1:{'name':name, 'price':price, 'stock':stock}}
        print(f'{name} added successfully!')
        return True
    def remove_product(self, product_id):
        if product_id in self.content:
            product_name = self.content.get(product_id).get('name')
            self.content.__delitem__(product_id)
            print(f'{product_name} removed successfully!')
            return True
        print(f'Product with id ({product_id}) does not exist')
        return False
    def update_product(self, product_id, name='', price=0, stock=0):
        if product_id in self.content:
            product_name = self.content.get(product_id).get('name')
            product = self.content.get(product_id)
            if name:
                product['name'] = name
            if price:
                product['price'] = price
            if stock:
                product['stock'] = stock
            # product['name'] = name if name else product['name']
            print(f'{product_name} updated successfully!')
            return True
        print(f'Product with id ({product_id}) does not exist')
        return False
    def get_product(self, product_id):
        if product_id in self.content:
            product = self.content.get(product_id)
            product['shop'] = self.name
            print(product)
            return True
        print(f'Product with id ({product_id}) does not exist')
        return False


# class Shoppingcart:

shop1 = Shop('IT Central')
shop1.add_product('iPhone X', 30000, 5)
shop1.add_product('iPhone 11 Pro', 30000, 5)
shop1.add_product('iPhone 5s', 30000, 5)
# shop1.get_product(1)
# shop1.remove_product(1)
print('\n')
print('\n')

shop2 = Shop('PY Gadgets')
shop2.add_product('Lenovo G20', 34000, 15)
shop2.add_product('HP iPhone', 34000, 15)
shop2.add_product('Microwave v2', 34000, 15)
# shop2.remove_product(2)
# shop2.update_product(1, 'Lenovo 190')
print('\n')
print('\n')

shop3 = Shop('MT Gadgets')
shop3.add_product('HP G20', 34000, 15)
shop3.add_product('Android G20', 34000, 15)
shop3.add_product('Samsung G20', 34000, 15)
shop3.add_product('Galaxy G20', 34000, 15)
# shop3.get_product(1)
# shop3.remove_product(1)

class Cart():
    '''
    A Shopping Cart Class:
        content: dict()
    Attributes:
        add_product: returns dict()
        show: returns dict()
    '''
    def __init__(self):
        self.content = {}
        # {'IT Central':[{'id':1, 'name':'Apple', 'unit':2}], 'MT Gadgets':[{}]}
        # {'shopname':{1:{'name':'Apple'}}}
    def add_product(self, shop, id, unit):
        product = {'name':shop.content.get(id).get('name'), 'unit':unit}
        if unit <= shop.content.get(id).get('stock'):
            shop.content[id]['stock'] -= unit
            if shop.name in self.content:
                if id in self.content[shop.name]:
                    self.content[shop.name][id]['unit'] += unit
                else:
                    self.content[shop.name][id] = product
                print(product.get('name'), 'added to cart successfully!')
                return True
            self.content[shop.name] = {id:product}
            print(product.get('name'), 'added to cart successfully!')
            return True
        print('Unit exceeds available stock')
        return False
    def show(self):
        print(self.content)
        return self.content

print('\n')
print('\n')
print('\n')
print('\n')

cart1 = Cart()
shops = [shop1, shop2, shop3]
for i in range(len(shops)):
    shop = random.choice(shops)
    product_id = random.choice(list(shop.content))
    shop.get_product(product_id)
    cart1.add_product(shop, product_id, 3)
print('\n')
print('\n')
cart1.show()