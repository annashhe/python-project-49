from random import randint


TASK = 'Answer "yes" if the number is even, otherwise answer "no".'
MAX_NUMBER = 100  # maximum number


def generate_question_and_answer():
    number = randint(1, MAX_NUMBER)
    question = f'{number}'
    if is_even(number):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return question, correct_answer


def is_even(number):
    return number % 2 == 0
