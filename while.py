# import random
from random import randint, choice

# print(random.randint(10,100))

# print(randint(10, 100))

#Question
"""
create three empty lists
and assign them to the variables;
primes, evens and odds. Using the randint 
function add 5 corresponding numbers to 
the lists.
"""

primes = []

evens = []

odds = []

while len(primes) < 5 or len(evens) < 5 or len(odds) < 5:
    digit = randint(3, 99)
    is_prime = True
    for i in range(2, digit):
        if digit%i == 0:
            is_prime = False
            break
    if is_prime and len(primes) < 5:
        primes.append(digit)
    if digit%2 == 0:
        if len(evens) < 5:
            evens.append(digit)
    else:
        if len(odds) < 5:
            odds.append(digit)

print("primes: ", primes)
print("evens: ", evens)
print("odds: ", odds)

print('\n')
print('\n')
print('\n')
print('\n')


#Question Two
question_bank = [
    {'subject':'Basic Science', 
    'level':'js one',
     'topic':'gravity',
      'question':'What is gravity'}, 
      
      {'subject':'Basic Technology', 
    'level':'js one',
     'topic':'pc',
      'question':'What is the difference between a pc and a mac'},
      
      {'subject':'Basic Science', 
    'level':'js one',
     'topic':'skeleton',
      'question':'How many bones does the human finger have?'},

      {'subject':'Basic Technology', 
    'level':'js one',
     'topic':'operating system',
      'question':'Which of the following is an operating system?'},

      {'subject':'Basic Science', 
    'level':'js one',
     'topic':'respiration',
      'question':'Which of the following is a respiratory organ?'}
    ]

total = 3 #number of questions to get from bank
topics = [{'pc':1}, {'operating system':1}, {'drive':1}]
subject = 'Basic Technology'
level = 'js one'

questions = []

# while total > 0:
#     print('its working')
#     total -= 1

while total:
    # loop through all topics by creating a topic var.
    for topic in topics:
        # get the topic and assign it to a var. topic_title
        topic_title = list(topic.keys())[0]
        # get the number of questions from the topic
        number_of_qs = topic.get(topic_title)
        for i in range(number_of_qs):
            #range(number_of_qs) = [0]
            for question in question_bank:
                #question stands for each dict in question_bank
                if question.get('subject') == subject\
                    and question.get('level') == level\
                        and question.get('topic') == topic_title:
                    questions.append(question.get('question'))
            total -=1
    
print(questions)

print('\n')
print('\n')
print('\n')
#Question 4
"""
Create a question bank that hold 5 questions, each
question should have the following attributes:
subject, class, topic, options and the question itself.

Create a while loop that will run and generate 3
questions from the question bank. The while loop
should only stop if all 3 questions
have been found or if it cant find anymore questions.

print your generated questions at the end.
"""

qb = [
    {'subject':'english',
    'class':'primary six',
    'topic':'verbs',
    'question':'Ali likes to jump when no one\'s around. jump in the sentence above is a/an _______?',
    'options':['pronoun', 'adverb', 'adjective', 'verb']
    },
    {'subject':'english',
    'class':'primary six',
    'topic':'pronouns',
    'question':'He is a very naughty boy. He in the sentence above is a/an _______?',
    'options':['pronoun', 'adverb', 'adjective', 'verb']
    },
    {'subject':'english',
    'class':'primary six',
    'topic':'adjectives',
    'question':'Ali sings beautifully. beautifully in the sentence above is a/an _______?',
    'options':['pronoun', 'adverb', 'adjective', 'verb']
    },
    {'subject':'english',
    'class':'primary six',
    'topic':'sentences',
    'question':'Ali the man. This is a complete sentence',
    'options':['False', 'True']
    },
    {'subject':'english',
    'class':'primary six',
    'topic':'tenses',
    'question':"'Sat', 'Left', 'Told' all are past tenses",
    'options':['False', 'True']
    }
]

qs_needed = 3
generated_qs = []

while qs_needed > 0:
    q = choice(qb)
    if q.get('question') not in generated_qs:
        generated_qs.append(q.get('question'))
        qs_needed -= 1

print(len(generated_qs))
print(generated_qs)

print('\n')
print('\n')
print('\n')
print('\n')

# Question 5
'''
Using the qb above generate topic based questions
of your choice.
'''

topics = {'verbs':1, 'adjectives':1, 'tenses':1}
total_qs = 3
gqs = []

while total_qs > 0:
    for t in topics:
        for q in qb:
            if q.get('topic') == t:
                gqs.append(q.get('question'))
        total_qs -= 1

print(len(gqs))
print(gqs)