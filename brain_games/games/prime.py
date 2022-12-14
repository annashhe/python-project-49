from random import randint


task = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def question_answer():
    number = randint(1, 100)
    question = f'''Question: {number}'''
    i = 0
    for n in range(2, number // 2 + 1):
        if (number % n == 0):
            i += 1
    if i > 0:
        correct_answer = 'no'
    else:
        correct_answer = 'yes'
    return question, correct_answer
