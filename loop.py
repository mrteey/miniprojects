# List of students in python class
students = ['Ahmad', 'Mohd', 'Abdul', 'Abdul2', 'Alex', 'Abdul3', 'Random']

print(students[0])
print(students[1])
print(students[2])
print(students[3])
print(students[4])
print(students[5])

new = []
print(students[:3])
for xxx in students:
    new.append(xxx)
print(new)
print('\n')
print(xxx)

for i in xxx:
    print(i)
print('\n')
print(i)

print('\n')
print('\n')

me = 'Maska'

for i in me:
    print(i)

print('\n')
print('\n')

mm = {'people':['Abdul', 'Bashir'], 'fruits':['mango', 'banana'], 'animals':['cat', 'dog']}

for m in mm:
    print(m, ': \n')
    for i in mm.get(m):
        print(i)
        print('\n')
        for x in i:
            print(x)
    print('\n')


data = ['Apple', 'Banana', 'Cup', 'Ball', 'Air', 'Class', 'Diamond']

alphabets = {'A':[], 'B':[], 'C':[], 'D':[]}

for d in data:
    if d[0] in alphabets:
        alphabets[d[0]].append(d)

print(alphabets)

data2 = ['Banana', 'Apple', 'Cup', 'Ball', 'Air', 'Class', 'Diamond', 'Silver', 'Baloon', 'Chicken', 'PS2']
alphabets2 = {}

data2.sort()
for d in data2:
    if d[0] not in alphabets2:
        alphabets2[d[0]] = []
    alphabets2[d[0]].append(d)
print('\n')
print('\n')
print('\n')
print('alphabests2: ',alphabets2)




people = ['Haidar', 'Aisha', 'Bello', 'Bashir']

a = {}

for person in people:
    if person[0] not in a:
        a[person[0]] = []
    a[person[0]].append(person)
print(a)

#Assignment 1

"""
create four variables 
data, people, animals and fruits.
The variable data should hold this data {'fruits':
['mango', 'banana'], 'people':['ahmad', 'alex'],
'animals':['dog', 'cat']}. The other variables can be 
an empty list, empty tuple or a string which ever one.
Loop through the variable data
check if the current object in loop 
is a fruit and add it to the fruits variable,
check if the current object 
in loop is a person and add 
it to the people variable,
check if the current object 
in loop is an animal and add 
it to the animals variable,
"""

data = {'fruits':
['mango', 'banana'], 'people':['ahmad', 'alex'],
'animals':['dog', 'cat']}
people, animals, fruits = [], (), ""

for i in data:
    if i == 'people':
        people.extend(data.get(i))
    elif i == 'animals':
        animals = tuple(data.get(i))
    else:
        for fruit in data.get(i):
            fruits+=fruit+', '
print('\n')
print('\n')
print('\n')
print(people)
print(animals)
print(fruits)

print('\n')
print('\n')
print('\n')

counter = 10
while counter > 5:
    print('Ahmad')
    print('counter: ',counter)
    counter -= 1

