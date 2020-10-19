# import random
from random import randint

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